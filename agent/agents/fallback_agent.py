from agents.base_agent import BaseAgent


class FallbackAgent(BaseAgent):
    agent_type = "fallback"
    event_label = "General Event"
    tone = "Professional and helpful."
    venue_knowledge = ""
    menu_knowledge = ""
    vendor_knowledge = ""
    artist_knowledge = ""
    personalization_questions = []
    operational_timeline = ""
