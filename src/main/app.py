from src.main.infra.utils.log_utils import log
from src.main.infra.config.notification_provider_config import create_notification_providers
from src.main.domain.models.user_model import UserModel
from src.main.domain.models.event_model import EventModel
from src.main.domain.repositories.user_repository import UserRepository
from src.main.domain.repositories.event_repository import EventRepository
from src.main.business.notification.provider.notification_provider_i import NotificationProviderI
from src.main.business.notification.registry.notification_provider_registry import NotificationProviderRegistry


class App:
    def __init__(self):
        self._user_repository: UserRepository = UserRepository()
        self._event_repository: EventRepository = EventRepository()
        self._notification_registry: NotificationProviderRegistry = create_notification_providers()

    def run(self) -> None:
        users: list[UserModel] = self._user_repository.get_all_users()
        for user in users:
            events: list[EventModel] = self._event_repository.get_all_by_user(user)
            choosen_providers: list[str] = user.providers
            
            notification_providers: list[NotificationProviderI] = (
                self._notification_registry.get_choosen_providers(provider_keys=choosen_providers))
            
            for provider in notification_providers:
                try:
                    log.info(
                        '%s - Notifying user: %s with provider %s', 
                        self.__class__.__name__, 
                        user.full_name, 
                        provider.__class__.__name__
                    )
                    provider.notify(events, user)
                except Exception as e:
                    log.error("Error notifying %s: %s", user.full_name, e)
