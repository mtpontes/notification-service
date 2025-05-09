from src.main.business.publisher.publisher_i import PublisherI
from src.main.business.publisher.sns_publisher_impl import SNSPublisherImpl
from src.main.domain.models.user_model import UserModel
from src.main.domain.models.event_model import EventModel
from src.main.domain.repositories.user_repository_i import UserRepositoryI
from src.main.domain.repositories.event_repository_i import EventRepositoryI
from src.main.infra.utils.log_utils import log
from src.main.infra.providers.notificarion_provider_enum import NotificationProviderEnum
from src.main.infra.db.repositories.mongodb_user_repository_impl import MongodbUserRepositoryImpl
from src.main.infra.db.repositories.mongodb_event_repository_impl import MongodbEventRepositoryImpl


class App:
    def __init__(self):
        log.info('%s - Start constructor', self.__class__.__name__)
        
        self._user_repository: UserRepositoryI = MongodbUserRepositoryImpl()
        self._event_repository: EventRepositoryI = MongodbEventRepositoryImpl()
        self._publisher: PublisherI = SNSPublisherImpl()
        
        log.info('%s - End constructor', self.__class__.__name__)

    def run(self) -> None:
        log.info('%s - [run] - Start', self.__class__.__name__)

        users: list[UserModel] = self._user_repository.find_all()
        for user in users:
            log.info('%s - [run] - Current user: %s', self.__class__.__name__, user)
            events: list[EventModel] = self._event_repository.find_all_by_user(user.id)
            
            for provider in user.providers:
                log.info('%s - [run] - Current provider: %s', self.__class__.__name__, provider)
                provider_enum: NotificationProviderEnum = None
                try:
                    provider_enum = NotificationProviderEnum(provider.upper())
                    self._publisher.publish(events, user, provider_enum)
                    log.info('%s - [run] - End', self.__class__.__name__)
                    
                except Exception as e:
                    log.error("Error notifying %s: %s", user.full_name, e)
