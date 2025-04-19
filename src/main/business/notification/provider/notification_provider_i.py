from abc import ABC, abstractmethod

from src.main.domain.models.user_model import UserModel
from src.main.domain.models.event_model import EventModel

class NotificationProviderI(ABC):  # Interface
    @abstractmethod
    def notify(self, events: list[EventModel], user: UserModel) -> None:
        raise NotImplementedError('Required method')
