from src.main.app import App
from src.main.infra.config.app_config import AppConfig
from src.main.infra.environment.dot_env_utils import DotEnvUtils
from src.main.infra.db.database_connection_i import DatabaseConnectionI
from src.main.infra.db.mongo_database_connection_impl import MongoDatabaseConnectionImpl


DotEnvUtils.load()                              # Carrega envs
AppConfig.load()                                # Carrega configurações

db_conn: DatabaseConnectionI = MongoDatabaseConnectionImpl()# Conecta ao banco de dados
db_conn.connect()

App().run()                                     # Inicia a aplicação

db_conn.close()