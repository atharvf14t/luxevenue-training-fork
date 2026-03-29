from agents.base_agent import BaseAgent
from knowledge import strategy_power_meets_kb as kb


class StrategyPowerMeetsAgent(BaseAgent):
    agent_type = kb.AGENT_TYPE
    event_label = kb.EVENT_LABEL
    tone = kb.TONE
    venue_knowledge = kb.VENUE_KNOWLEDGE
    menu_knowledge = kb.MENU_KNOWLEDGE
    vendor_knowledge = kb.VENDOR_KNOWLEDGE
    artist_knowledge = kb.ARTIST_KNOWLEDGE
    personalization_questions = kb.PERSONALIZATION_QUESTIONS
    operational_timeline = kb.OPERATIONAL_TIMELINE
