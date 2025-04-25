from src.main.infra.utils.log_utils import log
from src.main.business.notification.provider.notification_provider_i import NotificationProviderI


class NotificationProviderRegistry:
    def __init__(self):
        self._providers: dict[str, NotificationProviderI] = {}

    def register(self, provider_name: str, implementation: NotificationProviderI):
        self._providers[provider_name] = implementation
        return self

    def get_choosen_providers(self, provider_keys: list[str]) -> list[NotificationProviderI]:
        log.info('%s - Providers: %s', self.__class__.__name__, self._providers)
        providers = []
        for name in provider_keys:
            provider = self._providers.get(name)
            providers.append(provider)
        return providers