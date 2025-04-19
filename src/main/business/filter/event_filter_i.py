from abc import ABC, abstractmethod

from src.main.domain.models.event_model import EventModel


class EventFilterI(ABC):  # Interface
    @abstractmethod
    def filter_events(self, events: list[EventModel]) -> list[EventModel]:
        raise NotImplementedError('Required method')
