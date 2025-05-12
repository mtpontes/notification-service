import os
from dataclasses import dataclass

from src.main.infra.environment.environment_consts import EnvDatabaseConsts


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
            uri=os.getenv(EnvDatabaseConsts.DB_URI, 'mongodb://localhost:27017'),
            username=os.getenv(EnvDatabaseConsts.DB_USERNAME, 'admin'),
            password=os.getenv(EnvDatabaseConsts.DB_PASSWORD, 'admin'),
            database=os.getenv(EnvDatabaseConsts.DB_NAME),
            uri_args=os.getenv(EnvDatabaseConsts.DB_URI_ARGS),
        )
    
    def build_connection_string(self) -> str:
        return f'mongodb+srv://{self.username}:{self.password}@{self.uri}/{self.uri_args}'