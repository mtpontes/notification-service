from typing import ClassVar

from dotenv import load_dotenv

from src.main.infra.config.configs import SecretManagerConfig, DatabaseConfig, WhatsappConfig 


class AppConfig:
    mongo: ClassVar[DatabaseConfig]
    whatsapp: ClassVar[WhatsappConfig]
    secret_manager: ClassVar[SecretManagerConfig]
    enabled_providers: ClassVar[list[str]]

    __loaded: ClassVar[bool] = False

    @classmethod
    def load(cls):
        if cls.__loaded:
            return cls
        load_dotenv()

        cls.mongo = DatabaseConfig.load_from_env()
        cls.whatsapp = WhatsappConfig.load_from_env()
        cls.secret_manager = SecretManagerConfig.load_from_env()

        cls.__loaded = True
        return cls
