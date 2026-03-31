"""Abstract base class for all LuxeVenue event agents."""
from abc import ABC, abstractmethod
from typing import Optional


class BaseAgent(ABC):
    @property
    @abstractmethod
    def agent_type(self) -> str: ...

    @property
    @abstractmethod
    def event_label(self) -> str: ...

    @property
    @abstractmethod
    def tone(self) -> str: ...

    @property
    @abstractmethod
    def venue_knowledge(self) -> str: ...

    @property
    @abstractmethod
    def menu_knowledge(self) -> str: ...

    @property
    @abstractmethod
    def vendor_knowledge(self) -> str: ...

    @property
    @abstractmethod
    def artist_knowledge(self) -> str: ...

    @property
    @abstractmethod
    def personalization_questions(self) -> list[str]: ...

    @property
    @abstractmethod
    def operational_timeline(self) -> str: ...

    def address_user(self, user_name: str, user_gender: str) -> str:
        if user_gender == "male":
            return f"{user_name}, sir"
        elif user_gender == "female":
            return f"{user_name}, ma'am"
        return user_name
