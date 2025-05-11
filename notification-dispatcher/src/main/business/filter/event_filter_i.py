from abc import ABC, abstractmethod

from src.main.domain.event_model import EventDTO


class EventFilterI(ABC):  # Interface
    @abstractmethod
    def filter_events(self, events: list[EventDTO]) -> list[EventDTO]:
        raise NotImplementedError('Required method')
