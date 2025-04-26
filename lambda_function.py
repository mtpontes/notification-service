from src.main.app import App
from src.main.infra.config.app_config import AppConfig
from src.main.infra.db.database_connection_i import DatabaseConnectionI
from src.main.infra.db.mongo_database_connection_impl import MongoDatabaseConnectionImpl

def lambda_handler(event, _):
    AppConfig.load()  # Carrega configurações

    db_conn: DatabaseConnectionI = MongoDatabaseConnectionImpl()
    db_conn.connect() # Conecta ao banco de dados

    App().run()       # Inicia a aplicação

    db_conn.close()   # Fecha conexão com banco

if __name__ == "__main__":
    lambda_handler('', '')