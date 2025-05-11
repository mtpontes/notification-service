import os
from typing import ClassVar

from dotenv import load_dotenv

from src.main.infra.integration.integration_configs import WhatsappConfig, SecretManagerConfig


class AppConfig:
    whatsapp: ClassVar[WhatsappConfig]
    secret_manager: ClassVar[SecretManagerConfig]

    __loaded: ClassVar[bool] = False

    @classmethod
    def load(cls):
        if cls.__loaded:
            return cls
        
        if os.getenv('ENVIRONMENT', '') not in ('PRD', 'DEV'):
            load_dotenv()

        cls.whatsapp = WhatsappConfig.load_from_env()
        cls.secret_manager = SecretManagerConfig.load_from_env()

        cls.__loaded = True
        return cls