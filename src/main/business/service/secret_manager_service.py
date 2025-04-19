import json

from boto3.session import Session
from botocore.exceptions import ClientError

from src.main.infra.config.app_config import AppConfig


class SecretManagerService():

    def __init__(self):
        region: str = AppConfig.secret_manager.region
        self.client = Session().client(service_name='secretsmanager', region_name=region)

    def get_secret(self, secret_name: str) -> dict: # TODO : tratar erros de credenciais - 1
        result = self.client.get_secret_value(SecretId=secret_name)
        secrets = result['SecretString']
        if secrets is not None:
            return json.loads(secrets)
        raise Exception("Secret not found")
        
    def update_secret(self, secret_name: str, secrets_key_value: dict) -> None:
        try:
            self.client.put_secret_value(
                SecretId=secret_name,
                SecretString=json.dumps(secrets_key_value), # Deve ser um json
            )
        except ClientError as e: # TODO : tratar erros de credenciais - 2
            pass
        except Exception as e:
            pass