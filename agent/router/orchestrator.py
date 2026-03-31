"""
LuxeVenue Multi-Agent Orchestrator.

Architecture:
- StateGraph with a single "main_node" that does everything per turn
- LangGraph AsyncPostgresSaver checkpoints state keyed by session_id (thread_id)
- The main_node uses the agent's knowledge + current_phase to generate a response
- Streaming is provided via astream_events()
"""
import json
import re
from datetime import datetime, timezone
from typing import AsyncGenerator

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import AzureChatOpenAI
from langgraph.graph import END, StateGraph
from langgraph.checkpoint.memory import MemorySaver

from agents.base_agent import BaseAgent
from agents.strategy_power_meets_agent import StrategyPowerMeetsAgent
from agents.board_meeting_agent import BoardMeetingAgent
from agents.agm_agent import AGMAgent
from agents.leadership_summit_agent import LeadershipSummitAgent
from agents.conference_seminar_agent import ConferenceSeminarAgent
from agents.workshop_training_agent import WorkshopTrainingAgent
from agents.symposium_agent import SymposiumAgent
from agents.award_night_gala_agent import AwardNightGalaAgent
from agents.success_party_agent import SuccessPartyAgent
from agents.product_launch_agent import ProductLaunchAgent
from agents.offsite_agent import OffsiteAgent
from agents.team_building_agent import TeamBuildingAgent
from agents.cocktail_night_agent import CocktailNightAgent
from agents.fallback_agent import FallbackAgent
from core.config import settings
from core.email_service import send_inquiry_email
from knowledge.base_knowledge import BASE_LUXEVENUE_KNOWLEDGE
from state.conversation_state import ConversationState
from tools.marker_builders import (
    build_artist_cards_marker,
    build_chips_marker,
    build_menu_cards_marker,
    build_venue_cards_marker,
    build_vendor_cards_marker,
)
from tools.venue_tools import search_venues
from tools.artist_tools import get_artists_for_event
from tools.vendor_tools import get_vendors_for_event

# ─── Agent registry ───────────────────────────────────────────────────────────

AGENTS: dict[str, BaseAgent] = {
    "strategy_power_meets": StrategyPowerMeetsAgent(),
    "board_meeting": BoardMeetingAgent(),
    "agm": AGMAgent(),
    "leadership_summit": LeadershipSummitAgent(),
    "conference_seminar": ConferenceSeminarAgent(),
    "workshop_training": WorkshopTrainingAgent(),
    "symposium": SymposiumAgent(),
    "award_night_gala": AwardNightGalaAgent(),
    "success_party": SuccessPartyAgent(),
    "product_launch": ProductLaunchAgent(),
    "offsite": OffsiteAgent(),
    "team_building": TeamBuildingAgent(),
    "cocktail_night": CocktailNightAgent(),
    "fallback": FallbackAgent(),
}

# ─── LLM client ───────────────────────────────────────────────────────────────

def get_llm(streaming: bool = True) -> AzureChatOpenAI:
    return AzureChatOpenAI(
        azure_endpoint=settings.azure_openai_endpoint,
        azure_deployment=settings.azure_openai_deployment,
        api_key=settings.azure_openai_api_key,
        api_version=settings.azure_openai_api_version,
        streaming=streaming,
        temperature=0.7,
    )


# ─── Intent classification ────────────────────────────────────────────────────

CLASSIFICATION_PROMPT = """Classify the user's intent for a luxury corporate event planning platform.
Respond with exactly ONE of these labels (no explanation):
- strategy_power_meets  (strategy meetings, power meets, executive roundtables, leadership offsite)
- board_meeting         (board meetings, directors meetings, quarterly board)
- agm                   (annual general meeting, AGM, shareholder meeting)
- leadership_summit     (leadership summit, CXO summit, CEO forum, leadership conference)
- conference_seminar    (conferences, seminars, industry events, knowledge sharing events, professional summits)
- workshop_training     (workshops, training sessions, skill development, hands-on learning, team training)
- symposium             (symposiums, academic events, research presentations, expert panels, scholarly discussions)
- award_night_gala      (award nights, galas, award ceremonies, recognition events, achievement nights)
- success_party         (success parties, celebration parties, milestone parties, team parties, victory parties)
- product_launch        (product launches, brand launches, new product reveal, launch events, product unveiling)
- offsite               (offsites, corporate retreats, resort trips, team getaways, team trips, company retreats)
- team_building         (team building, team activities, corporate games, bonding activities, group challenges, team games)
- cocktail_night        (cocktail nights, cocktail events, networking drinks, corporate bar night, mixology events)
- fallback              (weddings, birthdays, social events, or unclear)

User message: {message}"""


async def classify_intent(message: str) -> str:
    llm = get_llm(streaming=False)
    response = await llm.ainvoke(
        [SystemMessage(content=CLASSIFICATION_PROMPT.format(message=message))]
    )
    label = response.content.strip().lower().replace(" ", "_").replace("-", "_")
    label = label.strip("-_ \t\n")
    return label if label in AGENTS else "fallback"


# ─── State extraction helpers ─────────────────────────────────────────────────

def extract_city(text: str) -> str | None:
    """Detect Indian city names from user input."""
    cities = [
        "mumbai", "delhi", "new delhi", "bangalore", "bengaluru", "hyderabad",
        "chennai", "kolkata", "pune", "ahmedabad", "jaipur", "surat", "lucknow",
        "kanpur", "nagpur", "indore", "thane", "bhopal", "visakhapatnam", "gurgaon",
        "gurugram", "noida", "chandigarh", "coimbatore", "kochi", "cochin",
        "agra", "vadodara", "rajkot", "patna", "guwahati", "raipur", "udaipur",
        "jodhpur", "amritsar", "srinagar", "dehradun", "shimla", "mysore", "mysuru",
    ]
    lower = text.lower()
    for city in cities:
        if city in lower:
            return city.title()
    return None


def extract_guest_count(text: str) -> int | None:
    """Extract numeric guest count from text."""
    patterns = [
        r"(\d+)\s*(?:guests?|people|attendees?|pax|members?|delegates?|shareholders?|directors?|participants?|executives?|leaders?|ceos?|cxos?|persons?|heads?|professionals?|invitees?)",
        r"(?:for|around|about|approx\.?|approximately|expect(?:ing)?|anticipat(?:ing)?)\s*(\d+)",
        r"(\d+)\s*(?:of us|colleagues?|professionals?|employees?)",
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return int(match.group(1))
    return None


def extract_event_date(text: str) -> str | None:
    """Simple date extraction for DD Month YYYY or YYYY-MM-DD patterns."""
    patterns = [
        r"\b(\d{1,2})\s+(jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|jun(?:e)?|jul(?:y)?|aug(?:ust)?|sep(?:tember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)\s+(\d{4})\b",
        r"\b(\d{4})-(\d{2})-(\d{2})\b",
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(0)
    return None


def detect_venue_selection(message: str) -> str | None:
    """Detect if user is booking/selecting a specific venue."""
    patterns = [
        r"(?:book|select|i want to book|i'd like to book|booking|finalise|finalize)\s+(.+?)(?:\s+(?:hotel|venue|property|banquet|ballroom))?\s*$",
        r"(?:go with|going with|choosing|choose|we'll go with)\s+(.+?)(?:\s+(?:hotel|venue|property))?\s*$",
        r"i (?:want|would like) (?:the|to book)\s+(.+?)(?:\s+(?:hotel|venue|property))?\s*$",
    ]
    for pattern in patterns:
        match = re.search(pattern, message, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    return None


def detect_menu_selection(message: str) -> str | None:
    """Detect if user is choosing a menu tier."""
    patterns = [
        r"(?:i choose|choose|selecting|select|go with|i'll take|i want)\s+(?:the\s+)?(.+?)\s+(?:menu|package|plan|tier)",
        r"(.+?)\s+(?:menu|package|plan|tier)\s+(?:please|works?|sounds? good|is fine)",
    ]
    for pattern in patterns:
        match = re.search(pattern, message, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    return None


def is_affirmative(message: str) -> bool:
    affirmatives = ["yes", "sure", "ok", "okay", "proceed", "go ahead", "next", "continue", "sounds good", "perfect", "great", "definitely", "absolutely"]
    lower = message.lower().strip()
    return any(a in lower for a in affirmatives)


# ─── System prompt builder ────────────────────────────────────────────────────

def build_system_prompt(
    agent: BaseAgent,
    state: ConversationState,
    phase_instruction: str,
) -> str:
    today = datetime.now(timezone.utc).strftime("%d %B %Y")
    user_addr = agent.address_user(state["user_name"], state["user_gender"])
    lang = state.get("language", "en")

    lang_rule = {
        "en": "Respond in English.",
        "hi": "Respond in Hindi (Devanagari script).",
        "hinglish": "Respond in Hinglish (mix of Hindi and English, as the user writes).",
    }.get(lang, "Respond in English.")

    return f"""{agent.tone}

USER CONTEXT:
- Name: {state['user_name']} | Address as: {user_addr}
- Language: {lang}. {lang_rule}
- Event Type: {state.get('event_type') or agent.event_label}
- City: {state.get('city') or 'Not yet provided'}
- Guest Count: {state.get('guest_count') or 'Not yet provided'}
- Event Date: {state.get('event_date') or 'Not yet provided'}
- Selected Venue: {state.get('selected_venue', {}).get('name', 'Not yet selected') if state.get('selected_venue') else 'Not yet selected'}
- Selected Menu: {state.get('selected_menu') or 'Not yet selected'}
- Today: {today}

{agent.venue_knowledge}

{agent.menu_knowledge}

{agent.vendor_knowledge}

{agent.artist_knowledge}

{BASE_LUXEVENUE_KNOWLEDGE}

CURRENT TASK:
{phase_instruction}

CRITICAL RULES:
- Never use emojis.
- Never output raw JSON or marker strings in plain text responses (no [VENUE_CARDS:] etc.) — those are added by the system separately.
- Address the user appropriately: {user_addr}
- Date validation: Today is {today}. Any event date in the past is invalid — politely ask for a future date.
- Respond in: {lang}
- When outputting [CHIPS: ...], use exactly this format: [CHIPS: Option1 | Option2 | Option3]
"""


# ─── Per-phase logic ──────────────────────────────────────────────────────────

async def handle_fallback(state: ConversationState) -> dict:
    """For unimplemented event types."""
    user_name = state["user_name"]
    response = (
        f"Thank you for reaching out, {user_name}. "
        "Our specialised planning module for this event type is currently under development "
        "and will be available very shortly.\n\n"
        "In the meantime, our concierge team would be delighted to assist you personally. "
        "Please share your requirements and we will connect you with the right specialist within 2 hours.\n\n"
        + build_chips_marker(["Share my requirements", "Speak to a concierge", "Learn about LuxeVenue"])
    )
    return {
        "messages": [AIMessage(content=response)],
        "current_phase": "fallback",
    }


async def handle_context_collection(
    agent: BaseAgent, state: ConversationState, last_user_message: str
) -> dict:
    """Ask for missing event details before suggesting venues."""
    missing = []
    if not state.get("city"):
        missing.append("city")
    if not state.get("guest_count"):
        missing.append("expected number of attendees")
    if not state.get("event_date"):
        missing.append("preferred date")

    phase_instruction = f"""
The user wants to plan a {agent.event_label}.
Missing event details: {', '.join(missing)}.
Ask for these details warmly and concisely. Ask all missing fields in one message.
Once all details are provided, you will suggest venues.
"""
    llm = get_llm(streaming=True)
    system = build_system_prompt(agent, state, phase_instruction)
    messages = _build_lc_messages(system, state)

    content = ""
    async for chunk in llm.astream(messages):
        content += chunk.content

    return {
        "messages": [AIMessage(content=content)],
        "current_phase": "collecting_context",
    }


async def handle_venue_suggestion(
    agent: BaseAgent, state: ConversationState
) -> dict:
    """Suggest venues with event-specific reasoning + [VENUE_CARDS: ...] marker."""
    city = state.get("city", "Mumbai")
    guest_count = state.get("guest_count", 50)

    venues = await search_venues(city=city, guest_count=guest_count)

    if not venues:
        venues_text = f"No venues found in {city} for {guest_count} guests. Try a nearby city."
        return {
            "messages": [AIMessage(content=venues_text)],
            "current_phase": "venue_shown",
        }

    venue_marker = build_venue_cards_marker(venues, guest_count)

    phase_instruction = f"""
Introduce the venue selection with 2-3 sentences explaining:
1. Why these venues are ideal for a {agent.event_label} in {city}
2. Key features to look for in a venue for this event type (based on your venue knowledge)
3. End with: "Here are the top venues in {city} for your {agent.event_label}:"

Do NOT list the venues yourself — the venue cards are shown automatically after your message.
Keep it expert, concise, and persuasive.
"""
    llm = get_llm(streaming=True)
    system = build_system_prompt(agent, state, phase_instruction)
    messages = _build_lc_messages(system, state)

    intro = ""
    async for chunk in llm.astream(messages):
        intro += chunk.content

    full_content = intro + "\n\n" + venue_marker

    return {
        "messages": [AIMessage(content=full_content)],
        "current_phase": "venue_shown",
    }


async def handle_venue_confirmed(
    agent: BaseAgent, state: ConversationState, venue_name: str
) -> dict:
    """Acknowledge venue selection and present menu cards."""
    # Try to find the venue details from existing messages context
    selected_venue = {"name": venue_name, "city": state.get("city", ""), "pricePerDayMin": 10000, "pricePerDayMax": 50000}

    # Try to find from DB for accurate pricing
    try:
        venues = await search_venues(city=state.get("city", ""), guest_count=state.get("guest_count", 50))
        for v in venues:
            if venue_name.lower() in v["name"].lower() or v["name"].lower() in venue_name.lower():
                selected_venue = v
                break
    except Exception:
        pass

    menu_marker = build_menu_cards_marker(
        venue_name=selected_venue["name"],
        city=selected_venue.get("city", state.get("city", "")),
        guest_count=state.get("guest_count", 50),
        price_min=selected_venue.get("pricePerDayMin", 10000),
        price_max=selected_venue.get("pricePerDayMax", 50000),
    )

    phase_instruction = f"""
The user has selected {selected_venue['name']} as their venue.
1. Briefly confirm this is an excellent choice (1 sentence with agent-appropriate reasoning).
2. Explain what kind of menu/catering is ideal for a {agent.event_label} (based on your menu knowledge).
3. End with: "Please select a menu package for your {state.get('guest_count', 50)} guests at {selected_venue['name']}:"

Keep it concise. The menu cards are shown automatically.
"""
    llm = get_llm(streaming=True)
    system = build_system_prompt(agent, state, phase_instruction)
    messages = _build_lc_messages(system, state)

    intro = ""
    async for chunk in llm.astream(messages):
        intro += chunk.content

    full_content = intro + "\n\n" + menu_marker

    return {
        "messages": [AIMessage(content=full_content)],
        "current_phase": "menu_shown",
        "selected_venue": selected_venue,
    }


async def handle_menu_confirmed(
    agent: BaseAgent, state: ConversationState, menu_tier: str
) -> dict:
    """Acknowledge menu selection and present vendor cards."""
    vendors = await get_vendors_for_event(agent.agent_type)
    vendor_marker = build_vendor_cards_marker(
        category=f"{agent.event_label} Vendors",
        vendors=vendors,
    )

    phase_instruction = f"""
The user has selected the '{menu_tier}' menu package.
1. Confirm the menu selection positively (1 sentence).
2. Explain which vendors are essential for a {agent.event_label} and why (based on your vendor knowledge). Be specific — name the vendor categories and give a one-line reason for each.
3. End with: "Here are the recommended vendors for your {agent.event_label}:"

Keep the vendor reasoning brief but expert. Show you understand the specific needs of this event type.
"""
    llm = get_llm(streaming=True)
    system = build_system_prompt(agent, state, phase_instruction)
    messages = _build_lc_messages(system, state)

    intro = ""
    async for chunk in llm.astream(messages):
        intro += chunk.content

    full_content = intro + "\n\n" + vendor_marker

    return {
        "messages": [AIMessage(content=full_content)],
        "current_phase": "vendors_shown",
        "selected_menu": menu_tier,
    }


async def handle_artist_suggestion(
    agent: BaseAgent, state: ConversationState
) -> dict:
    """Present artist recommendations with reasoning."""
    artists = await get_artists_for_event(agent.agent_type)
    artist_marker = build_artist_cards_marker(
        category=f"{agent.event_label} Entertainment",
        artists=artists,
    )

    phase_instruction = f"""
Present the entertainment/artist recommendations for a {agent.event_label}.
1. Briefly explain the role of entertainment in this event type (based on your artist knowledge). Be honest — if entertainment is secondary for this event type, say so.
2. Name the specific artist categories relevant to this event type and why.
3. End with: "Here are the recommended artists and entertainers for your {agent.event_label}:"

Be agent-specific. A board meeting has very different entertainment needs than a leadership summit.
"""
    llm = get_llm(streaming=True)
    system = build_system_prompt(agent, state, phase_instruction)
    messages = _build_lc_messages(system, state)

    intro = ""
    async for chunk in llm.astream(messages):
        intro += chunk.content

    full_content = intro + "\n\n" + artist_marker + "\n\n" + build_chips_marker(
        ["Continue to personalisation", "Skip artists", "Show vendors again"]
    )

    return {
        "messages": [AIMessage(content=full_content)],
        "current_phase": "artists_shown",
    }


async def handle_personalization(
    agent: BaseAgent, state: ConversationState, user_message: str
) -> dict:
    """Ask personalisation questions one at a time. Collect answers."""
    questions = agent.personalization_questions
    if not questions:
        # No personalisation questions — move to email
        return await handle_send_email(agent, state)

    current_index = state.get("personalization_index", 0)
    answers = state.get("personalization_answers", {})

    # Save the answer to the previous question if we have one
    if current_index > 0 and user_message.strip():
        prev_question = questions[current_index - 1]
        if prev_question not in answers:
            answers = dict(answers)
            answers[prev_question] = user_message.strip()

    # Check if all questions answered
    if current_index >= len(questions):
        # Move to email
        new_state: dict = {
            "messages": [],
            "personalization_answers": answers,
            "personalization_index": current_index,
            "current_phase": "personalizing",
        }
        email_result = await handle_send_email(agent, {**state, **new_state})
        email_result["personalization_answers"] = answers
        return email_result

    # Ask the current question
    question = questions[current_index]

    phase_instruction = f"""
You are collecting personalisation details for the {agent.event_label}.
Ask the following question naturally and conversationally (do not just copy-paste it):
Question to ask: "{question}"

If this is not the first question, briefly acknowledge the previous answer before asking the next one.
Keep your response to 2-3 sentences maximum.
"""
    llm = get_llm(streaming=True)
    system = build_system_prompt(agent, state, phase_instruction)
    messages = _build_lc_messages(system, state)

    content = ""
    async for chunk in llm.astream(messages):
        content += chunk.content

    return {
        "messages": [AIMessage(content=content)],
        "current_phase": "personalizing",
        "personalization_index": current_index + 1,
        "personalization_answers": answers,
    }


async def handle_send_email(agent: BaseAgent, state: ConversationState) -> dict:
    """Compile all collected data and send email to ronit@luxevenue.ai."""
    event_context = {
        "event_type": state.get("event_type") or agent.event_label,
        "city": state.get("city"),
        "guest_count": state.get("guest_count"),
        "event_date": state.get("event_date"),
    }

    # Send email in background (don't block the response)
    try:
        send_inquiry_email(
            agent_type=agent.agent_type,
            user_name=state["user_name"],
            event_context=event_context,
            personalization_answers=state.get("personalization_answers", {}),
            selected_venue=state.get("selected_venue"),
            selected_menu=state.get("selected_menu"),
        )
    except Exception as e:
        print(f"[Email] Error sending: {e}")

    phase_instruction = f"""
All planning details have been collected for the {agent.event_label}.
Write a warm, professional closing message:
1. Thank the user and confirm their event brief has been compiled.
2. Mention that the LuxeVenue team will be in touch within 24 hours to begin execution.
3. Ask if there is anything else you can assist with.

Keep it concise — 3-4 sentences maximum.
"""
    llm = get_llm(streaming=True)
    system = build_system_prompt(agent, state, phase_instruction)
    messages = _build_lc_messages(system, state)

    content = ""
    async for chunk in llm.astream(messages):
        content += chunk.content

    content += "\n\n" + build_chips_marker([
        "Show event timeline",
        "Add more vendors",
        "Start a new event",
    ])

    return {
        "messages": [AIMessage(content=content)],
        "current_phase": "done",
        "email_sent": True,
    }


async def handle_general_chat(
    agent: BaseAgent, state: ConversationState
) -> dict:
    """Handle general questions that don't fit a specific phase."""
    phase_instruction = """
Answer the user's question using your event-specific knowledge and the LuxeVenue knowledge base.
Be helpful, concise, and guide them back to the planning flow when appropriate.
"""
    llm = get_llm(streaming=True)
    system = build_system_prompt(agent, state, phase_instruction)
    messages = _build_lc_messages(system, state)

    content = ""
    async for chunk in llm.astream(messages):
        content += chunk.content

    return {
        "messages": [AIMessage(content=content)],
    }


def _build_lc_messages(system_prompt: str, state: ConversationState) -> list:
    """Build message list for LLM call from state history."""
    result = [SystemMessage(content=system_prompt)]
    for msg in state.get("messages", []):
        if isinstance(msg, (HumanMessage, AIMessage)):
            result.append(msg)
        elif isinstance(msg, dict):
            if msg.get("type") == "human":
                result.append(HumanMessage(content=msg["content"]))
            elif msg.get("type") == "ai":
                result.append(AIMessage(content=msg["content"]))
    return result


# ─── Main LangGraph node ──────────────────────────────────────────────────────

async def main_node(state: ConversationState) -> dict:
    """
    The single LangGraph node that handles every turn.
    Reads current_phase and state to decide what to do.
    """
    # Get the last user message
    last_user_message = ""
    for msg in reversed(state.get("messages", [])):
        if isinstance(msg, HumanMessage):
            last_user_message = msg.content
            break
        elif isinstance(msg, dict) and msg.get("type") == "human":
            last_user_message = msg["content"]
            break

    # ── Step 1: Classify agent on first turn ──────────────────────────────────
    agent_type = state.get("agent_type")
    if not agent_type:
        agent_type = await classify_intent(last_user_message)

    agent = AGENTS.get(agent_type, AGENTS["fallback"])

    # ── Step 2: Fallback — agent not yet implemented ──────────────────────────
    if agent_type == "fallback":
        result = await handle_fallback(state)
        result["agent_type"] = agent_type
        return result

    # ── Step 3: Extract context from current message ──────────────────────────
    updates: dict = {"agent_type": agent_type}

    if not state.get("city"):
        city = extract_city(last_user_message)
        if city:
            updates["city"] = city

    if not state.get("guest_count"):
        count = extract_guest_count(last_user_message)
        if count:
            updates["guest_count"] = count

    if not state.get("event_date"):
        date = extract_event_date(last_user_message)
        if date:
            updates["event_date"] = date

    if not state.get("event_type"):
        updates["event_type"] = agent.event_label

    # Merge updates into working state for this turn
    working_state: ConversationState = {**state, **updates}

    # ── Step 4: Determine current phase and route ─────────────────────────────
    # Default to "init" if this is the first turn (no checkpoint yet)
    current_phase = working_state.get("current_phase") or "init"

    has_context = bool(working_state.get("city") and working_state.get("guest_count"))

    # Check for venue selection (user clicks "Book This Venue")
    venue_name = detect_venue_selection(last_user_message)
    if venue_name and current_phase == "venue_shown":
        result = await handle_venue_confirmed(agent, working_state, venue_name)
        return {**updates, **result}

    # Check for menu selection
    menu_tier = detect_menu_selection(last_user_message)
    if menu_tier and current_phase == "menu_shown":
        result = await handle_menu_confirmed(agent, working_state, menu_tier)
        return {**updates, **result}

    # After vendors shown — move to artists
    if current_phase == "vendors_shown":
        result = await handle_artist_suggestion(agent, working_state)
        return {**updates, **result}

    # Continue personalisation (artists_shown = just showed artists, start questions now)
    if current_phase == "artists_shown" or (
        current_phase == "personalizing"
        and working_state.get("personalization_index", 0) <= len(agent.personalization_questions)
    ):
        result = await handle_personalization(agent, working_state, last_user_message)
        return {**updates, **result}

    # All context collected — suggest venues
    if has_context and current_phase in ("init", "collecting_context"):
        result = await handle_venue_suggestion(agent, working_state)
        return {**updates, **result}

    # Missing context — ask for it
    if current_phase in ("init", "collecting_context") or not has_context:
        result = await handle_context_collection(agent, working_state, last_user_message)
        return {**updates, **result}

    # General fallback for all other states
    result = await handle_general_chat(agent, working_state)
    return {**updates, **result}


# ─── Build and compile the graph ─────────────────────────────────────────────

def build_graph(checkpointer=None):
    graph = StateGraph(ConversationState)
    graph.add_node("main_node", main_node)
    graph.set_entry_point("main_node")
    graph.add_edge("main_node", END)

    if checkpointer:
        return graph.compile(checkpointer=checkpointer)
    return graph.compile(checkpointer=MemorySaver())


# ─── Orchestrator class ───────────────────────────────────────────────────────

class LuxeVenueOrchestrator:
    def __init__(self):
        # Use MemorySaver for now; route.ts will pass session_id as thread_id
        # For production: swap with AsyncPostgresSaver
        self._checkpointer = MemorySaver()
        self._graph = build_graph(self._checkpointer)

    async def setup_postgres_checkpointer(self, db_url: str):
        """Call at startup to swap to Postgres-backed state persistence."""
        try:
            from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver
            import psycopg

            conn = await psycopg.AsyncConnection.connect(db_url)
            checkpointer = AsyncPostgresSaver(conn)
            await checkpointer.setup()
            self._checkpointer = checkpointer
            self._graph = build_graph(checkpointer)
            print("[Orchestrator] Using AsyncPostgresSaver for state persistence.")
        except Exception as e:
            print(f"[Orchestrator] Falling back to MemorySaver: {e}")

    async def stream_response(
        self,
        session_id: str,
        message: str,
        user_name: str,
        user_gender: str,
        language: str,
        user_id: str,
    ) -> AsyncGenerator[str, None]:
        """
        Main entry point: streams the AI response for a given user message.
        LangGraph restores previous state from checkpoint via thread_id=session_id.
        """
        config = {"configurable": {"thread_id": session_id}}

        # Only pass fields that should update every turn.
        # Fields like current_phase, agent_type, selected_venue etc. are preserved
        # automatically from the LangGraph checkpoint — do NOT override them here.
        input_data: dict = {
            "messages": [HumanMessage(content=message)],
            "user_name": user_name,
            "user_gender": user_gender,
            "language": language,
            "session_id": session_id,
            "user_id": user_id,
        }

        # Track what was streamed via on_chat_model_stream
        streamed_content = ""

        async for event in self._graph.astream_events(input_data, config, version="v2"):
            kind = event.get("event", "")

            if kind == "on_chat_model_stream":
                chunk = event["data"].get("chunk")
                if chunk and hasattr(chunk, "content") and chunk.content:
                    streamed_content += chunk.content
                    yield chunk.content

        # After graph completes, yield any marker suffix that wasn't streamed.
        # Markers ([VENUE_CARDS:], [MENU_CARDS:], etc.) are appended atomically
        # after the LLM stream in each node — they won't appear in on_chat_model_stream.
        try:
            checkpoint = await self._graph.aget_state(config)
            if checkpoint and checkpoint.values:
                msgs = checkpoint.values.get("messages", [])
                if msgs:
                    last_msg = msgs[-1]
                    if isinstance(last_msg, AIMessage):
                        full_content = last_msg.content
                    elif isinstance(last_msg, dict):
                        full_content = last_msg.get("content", "")
                    else:
                        full_content = ""

                    if full_content:
                        # Use rstripped streamed content for reliable comparison
                        # (LLM may add trailing newlines that differ from what the node stored)
                        streamed_stripped = streamed_content.rstrip()
                        if full_content.startswith(streamed_stripped):
                            suffix = full_content[len(streamed_stripped):]
                            if suffix.strip():  # only yield if there's actual content
                                yield suffix
        except Exception as e:
            print(f"[Orchestrator] Error getting state suffix: {e}")


# Global singleton
orchestrator = LuxeVenueOrchestrator()
