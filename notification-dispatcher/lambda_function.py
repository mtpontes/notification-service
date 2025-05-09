from dotenv import load_dotenv

from src.main.app import App
from src.main.infra.config.app_config import AppConfig


def lambda_handler(event, _):
    load_dotenv()
    AppConfig.load() # Carrega configurações
    App().run(event) # Inicia a aplicação


if __name__ == "__main__":
    lambda_handler('', '')