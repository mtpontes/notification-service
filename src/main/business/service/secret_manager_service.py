import json

from boto3.session import Session

from src.main.infra.config.app_config import AppConfig
from src.main.infra.environment.environment_consts import SecretManagerConsts


class SecretManagerService():

    def __init__(self):
        self.client = Session().client(
            service_name=SecretManagerConsts.SERVICE_NAME, 
            region_name=AppConfig.secret_manager.region
        )

    def get_secret(self, secret_name: str) -> dict:
        result: dict[str, any] = self.client.get_secret_value(SecretId=secret_name)
        secrets: str | None = result.get(SecretManagerConsts.SECRET_STRING)
        if secrets is not None:
            return json.loads(secrets)
        raise EmptySecretException("Secret not found")
        
    def update_secret(self, secret_name: str, secrets_key_value: dict) -> None:
        try:
            self.client.put_secret_value(
                SecretId=secret_name,
                SecretString=json.dumps(secrets_key_value), # Deve ser um json
            )
        except Exception as e:
            pass
        
class EmptySecretException(Exception):
    pass