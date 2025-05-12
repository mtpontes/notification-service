import json

from src.main.infra.utils.log_utils import log
from src.main.infra.providers.notificarion_provider_enum import NotificationProviderEnum


class PublisherUtils:
    @staticmethod    
    def create_message(provider: NotificationProviderEnum, events: list[dict], user: dict) -> str:
        dispatch = {
            'provider': provider.value,
            'events': events,
            'user': user
        }
        
        message: str = json.dumps(dispatch)
        log.info('%s - [create_message] - Created message: %s', PublisherUtils.__name__, message)
        return message