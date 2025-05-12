from abc import ABC, abstractmethod

from src.main.domain.user_model import UserDTO
from src.main.domain.event_model import EventDTO


class NotificationProviderI(ABC):  # Interface
    @abstractmethod
    def notify(self, events: list[EventDTO], user: UserDTO) -> None:
        raise NotImplementedError('Required method')
