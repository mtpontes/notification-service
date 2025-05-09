from abc import ABC, abstractmethod

from src.main.domain.models.user_model import UserModel
from src.main.domain.models.event_model import EventModel


class EventRepositoryI(ABC):

    @abstractmethod
    def find_all_by_user(self, user: UserModel) -> list[EventModel]:
        raise NotImplementedError('Required method')
