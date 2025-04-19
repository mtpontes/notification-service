from google.auth.exceptions import RefreshError
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

from src.main.infra.environment.environment_consts import GoogleCalendarConsts
from src.main.business.service.secret_manager_service import SecretManagerService


class TokenNotUpdatableError(Exception):
    pass


class GoogleCredentialManager:
    def __init__(self):
        self.__secret_manager_service = SecretManagerService()

    def get_valid_credentials(self, secret_key: str) -> Credentials:
        secret_value = self.__secret_manager_service.get_secret(secret_key)
        credentials: Credentials = self.__build_credentials(secret_value)
        credentials: Credentials = self.__resolve_credencials(credentials, secret_key)

        return credentials

    def __build_credentials(self, secret: dict) -> Credentials:
        return Credentials(
            token=secret[GoogleCalendarConsts.ACCESS_TOKEN],
            refresh_token=secret[GoogleCalendarConsts.REFRESH_TOKEN],
            client_id=secret[GoogleCalendarConsts.CLIENT_ID],
            client_secret=secret[GoogleCalendarConsts.CLIENT_SECRET],
            token_uri='https://oauth2.googleapis.com/token',
            scopes=['https://www.googleapis.com/auth/calendar']
        )

    def __resolve_credencials(self, credentials: Credentials, secret_key: str) -> Credentials:
        if not credentials.valid:
            if credentials.expired and credentials.refresh_token:
                try:
                    credentials = self.__update_credentials(credentials=credentials, secret_key=secret_key)
                except RefreshError as e:
                    raise TokenNotUpdatableError("Erro ao atualizar token.") from e
            else:
                raise Exception("Credenciais inválidas")
            
        return credentials
    
    def __update_credentials(self, credentials: Credentials, secret_key: str):
        credentials.refresh(Request())
        updated_secret = self.__extract_credential_data(credentials)
        self.__secret_manager_service.update_secret(secret_key, updated_secret)
        return credentials

    def __extract_credential_data(self, credentials: Credentials) -> dict:
        return {
            "access_token": credentials.token,
            "refresh_token": credentials.refresh_token,
            "client_id": credentials.client_id,
            "client_secret": credentials.client_secret
        }