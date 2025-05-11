import os
from dataclasses import dataclass

from src.main.infra.environment.environment_consts import DatabaseConsts


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