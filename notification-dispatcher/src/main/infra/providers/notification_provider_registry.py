from src.main.infra.utils.log_utils import log
from src.main.business.provider.notification_provider_i import NotificationProviderI
from src.main.infra.providers.notification_provider_enum import NotificationProviderEnum


class NotificationProviderRegistry:
    def __init__(self):
        self._providers: dict[NotificationProviderEnum, NotificationProviderI] = {}

    def register(self, key: NotificationProviderEnum, implementation: NotificationProviderI):
        self._providers[key] = implementation
        return self

    def get_choosen_provider(self, key: NotificationProviderEnum) -> NotificationProviderI | None:
        log.info('%s - [get_choosen_provider]: %s', self.__class__.__name__, self._providers)
        
        key_enum = next((e for e in NotificationProviderEnum if e.value == key), None)
        if key_enum:
            return self._providers.get(key_enum)
        return None