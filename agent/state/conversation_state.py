from typing import Annotated, Optional
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages


class ConversationState(TypedDict):
    # Full chat history — add_messages reducer appends new messages
    messages: Annotated[list, add_messages]

    # Routing — sticky: set on turn 1, never changed mid-session
    agent_type: Optional[str]  # strategy_power_meets | board_meeting | agm | leadership_summit | fallback

    # Current phase of the booking flow
    # init → venue_shown → menu_shown → vendors_shown → artists_shown → personalizing → done
    current_phase: str

    # Event context — collected incrementally
    event_type: Optional[str]
    city: Optional[str]
    guest_count: Optional[int]
    event_date: Optional[str]

    # User profile — passed from Next.js on every request
    user_name: str
    user_gender: str
    language: str

    # Booking progress
    selected_venue: Optional[dict]   # venue object from DB
    selected_menu: Optional[str]     # tier name chosen by user

    # Personalization tracking
    personalization_questions: list  # the agent's questions list
    personalization_index: int       # which question we're on
    personalization_answers: dict    # question_text → answer

    # Email
    email_sent: bool

    # Session identifiers (for LangGraph thread_id and logging)
    session_id: str
    user_id: str
