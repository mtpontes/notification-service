from abc import ABC, abstractmethod

from src.main.domain.models.user_model import UserModel
from src.main.domain.models.event_model import EventModel


class EventRepository(ABC):

    @abstractmethod
    def get_all_by_user(self, user: UserModel) -> list[EventModel]:
        pass