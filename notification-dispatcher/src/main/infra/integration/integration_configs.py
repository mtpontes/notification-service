import os
from dataclasses import dataclass

from src.main.infra.integration.integration_constants import WhatsappConsts, SecretManagerConsts


@dataclass(frozen=True)
class WhatsappConfig:
    api_token: str

    @staticmethod
    def load_from_env():
        return WhatsappConfig(api_token=os.getenv(WhatsappConsts.API_TOKEN, ''))


@dataclass(frozen=True)
class SecretManagerConfig:
    region: str

    @staticmethod
    def load_from_env():
        return SecretManagerConfig(region=os.getenv(SecretManagerConsts.REGION))