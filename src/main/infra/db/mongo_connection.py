import mongoengine

from src.main.infra.db.database_connection_i import DatabaseConnectionI
from src.main.infra.config.app_config import AppConfig, DatabaseConfig


class MongoConnection(DatabaseConnectionI):
    __mongo_client = mongoengine
    
    def connect(self):
        config: DatabaseConfig = AppConfig.mongo.load_from_env()
        
        database: str = config.database
        mongo_uri: str = config.build_connection_string()
        print(mongo_uri)

        self.__mongo_client.connect(db=database, host=mongo_uri)

    def close(self):
        self.__mongo_client.disconnect()