import os
from dataclasses import dataclass

from src.main.infra.environment.environment_consts import DatabaseConsts, WhatsappConsts, SecretManagerConsts


@dataclass(frozen=True)
class DatabaseConfig:
    uri: str
    username: str
    password: str
    database: str
    uri_args: str
    
    @staticmethod
    def load_from_env():
        return DatabaseConfig(
            uri=os.getenv(DatabaseConsts.DB_URI, 'mongodb://localhost:27017'),
            username=os.getenv(DatabaseConsts.DB_USERNAME, 'admin'),
            password=os.getenv(DatabaseConsts.DB_PASSWORD, 'admin'),
            database=os.getenv(DatabaseConsts.DB_NAME),
            uri_args=os.getenv(DatabaseConsts.DB_URI_ARGS),
        )
    
    def build_connection_string(self) -> str:
        return f'mongodb+srv://{self.username}:{self.password}@{self.uri}/{self.uri_args}'


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
