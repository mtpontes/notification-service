from abc import ABC, abstractmethod

from src.main.domain.models.user_model import UserModel
from src.main.domain.models.event_model import EventModel
from src.main.infra.providers.notificarion_provider_enum import NotificationProviderEnum

class PublisherI(ABC): # Interface

    @abstractmethod
    def publish(self, events: list[EventModel], user: UserModel, provider: NotificationProviderEnum) -> None:
        raise NotImplementedError('Required method')
