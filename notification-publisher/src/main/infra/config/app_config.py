import os
from typing import ClassVar

from dotenv import load_dotenv

from src.main.infra.config.environment_configs import DatabaseConfig


class AppConfig:
    mongo: ClassVar[DatabaseConfig]

    __loaded: ClassVar[bool] = False

    @classmethod
    def load(cls):
        if cls.__loaded:
            return cls
        
        if os.getenv('ENVIRONMENT', '') not in ('PRD', 'DEV'):
            load_dotenv()

        cls.mongo = DatabaseConfig.load_from_env()

        cls.__loaded = True
        return cls
