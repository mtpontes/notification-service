from src.main.business.notification.provider.notification_provider_i import NotificationProviderI


class NotificationProviderRegistry:
    def __init__(self):
        self.__providers: dict[str, NotificationProviderI] = {}

    def register(self, provider_name: str, implementation: NotificationProviderI):
        self.__providers[provider_name] = implementation
        return self

    def get_choosen_providers(self, provider_keys: list[str]) -> list[NotificationProviderI]:
        print(self.__providers)
        providers = []
        for name in provider_keys:
            provider = self.__providers.get(name)
            providers.append(provider)
        return providers