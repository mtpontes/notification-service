from src.main.business.application.app import App
from src.main.infra.config.app_config import AppConfig
from src.main.infra.db.mongo_connection import MongoConnection
from src.main.infra.environment.dot_env_utils import DotEnvUtils
from src.main.infra.db.database_connection_i import DataConnectionI


DotEnvUtils.load()                          # Carrega envs
AppConfig.load()                            # Carrega configurações

db_conn: DataConnectionI = MongoConnection() # Conecta ao banco de dados
db_conn.connect()

App().run()                                  # Inicia a aplicação