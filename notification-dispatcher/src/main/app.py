from src.main.business.provider.notification_provider_i import NotificationProviderI
from src.main.application.mapper import Mapper
from src.main.infra.utils.log_utils import log
from src.main.domain.user_model import UserDTO
from src.main.domain.event_model import EventDTO
from src.main.infra.utils.sns_utils import SNSUtils
from src.main.infra.constants.constants import LambdaEventConstants
from src.main.infra.providers.notification_provider_registry import NotificationProviderRegistry
from src.main.infra.providers.notification_provider_config import load_notification_provider_registry


class App:
    def __init__(self):
        log.info('%s - [constructor] - Start', self.__class__.__name__)
        
        self._mapper: Mapper = Mapper()
        self._notification_registry: NotificationProviderRegistry = load_notification_provider_registry()
        
        log.info('%s - [constructor] - End', self.__class__.__name__)

    def run(self, lambda_event) -> None:
        log.info('%s - [run] - Start', self.__class__.__name__)
        sns_message: dict = self._get_sns_message(lambda_event)
        
        provider_key: str = sns_message[LambdaEventConstants.PROVIDER]
        user: UserDTO = self._mapper.to_user_dto(sns_message[LambdaEventConstants.USER])
        events: list[EventDTO] = self._mapper.to_event_dto_list(sns_message[LambdaEventConstants.EVENTS])
        
        provider: NotificationProviderI = self._notification_registry.get_choosen_provider(provider_key)
        
        if not provider:
            log.error('%s - [run] - Provider not found', self.__class__.__name__)
            return 
    
        try:
            log.info('Notifying user: %s with provider %s', user.full_name, provider.__class__.__name__)
            provider.notify(events, user)
            log.info('%s - [run] - End', self.__class__.__name__)
        except Exception as e:
            log.error("%s - [run] - Error notifying %s: %s", self.__class__.__name__, user.full_name, e)

    def _get_sns_message(self, lambda_event: dict) -> dict:
        message: dict = SNSUtils.resolve_message(lambda_event)
        required_keys = [LambdaEventConstants.PROVIDER, LambdaEventConstants.USER, LambdaEventConstants.EVENTS]
        missing_keys = [key for key in required_keys if message.get(key) is None]
        
        if missing_keys:
            log.error('%s - [_get_sns_message] - Missing keys in SNS message: %s', self.__class__.__name__, missing_keys)
            raise ValueError(f"Missing or null keys in SNS message: {', '.join(missing_keys)}")
        
        log.info('%s - [_get_sns_message] - SNS Message: %s', self.__class__.__name__, message)
        return message
