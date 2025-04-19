import os
from typing import ClassVar

from src.main.infra.environment.environment_consts import EnvConsts
from src.main.infra.config.configs import SecretManagerConfig, DatabaseConfig, WhatsappConfig 


class AppConfig:
    mongo: ClassVar[DatabaseConfig]
    whatsapp: ClassVar[WhatsappConfig]
    secret_manager: ClassVar[SecretManagerConfig]
    enabled_providers: ClassVar[list[str]]

    __loaded: ClassVar[bool] = False

    @classmethod
    def load(cls) -> None:
        if cls.__loaded:
            return

        cls.mongo = DatabaseConfig.load_from_env()
        cls.whatsapp = WhatsappConfig.load_from_env()
        cls.secret_manager = SecretManagerConfig.load_from_env()
        cls.enabled_providers = os.getenv(EnvConsts.ENABLED_PROVIDERS, '').split(',')

        cls.__loaded = True
