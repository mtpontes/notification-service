from google.auth.exceptions import RefreshError
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

from src.main.infra.utils.log_utils import log
from src.main.infra.service.secret_manager_service import SecretManagerService
from src.main.infra.security.credentials_consts import GoogleCalendarCredentialsConsts


class TokenNotUpdatableError(Exception):
    def __init__(self, message: str = "Non-refreshable token"):
        super().__init__(message)


class GoogleCredentialManager:
    def __init__(self):
        log.info('%s - [constructor] - Start', self.__class__.__name__)
        
        self._secret_manager_service = SecretManagerService()
        log.info('Constructor - %s', self)
        
        log.info('%s - [constructor] - End - Self: %s', self.__class__.__name__, self)


    def __str__(self):
        return (
            f"{self.__class__.__name__}"
            f"(secret_manager_service='{self._secret_manager_service.__class__.__name__}')"
        )

    def get_valid_credentials(self, secret_key: str) -> Credentials:
        secret_value = self._secret_manager_service.get_secret(secret_key)
        credentials: Credentials = self._build_credentials(secret_value)
        credentials: Credentials = self._resolve_credencials(credentials, secret_key)
        return credentials

    def _build_credentials(self, secret: dict) -> Credentials:
        log.info('%s - _build_credentials', self.__class__.__name__)
        return Credentials(
            token=secret[GoogleCalendarCredentialsConsts.ACCESS_TOKEN],
            refresh_token=secret[GoogleCalendarCredentialsConsts.REFRESH_TOKEN],
            client_id=secret[GoogleCalendarCredentialsConsts.CLIENT_ID],
            client_secret=secret[GoogleCalendarCredentialsConsts.CLIENT_SECRET],
            token_uri='https://oauth2.googleapis.com/token',
            scopes=['https://www.googleapis.com/auth/calendar']
        )

    def _resolve_credencials(self, credentials: Credentials, secret_key: str) -> Credentials:
        log.info('%s - resolving credentials', self.__class__.__name__)
        if not credentials.valid:
            log.info('%s - token expired', self.__class__.__name__)
            if credentials.expired and credentials.refresh_token:
                try:
                    credentials = self._update_credentials(credentials=credentials, secret_key=secret_key)
                except RefreshError as e:
                    raise TokenNotUpdatableError("Erro ao atualizar token") from e
            else:
                raise Exception("Credenciais inválidas")
            
        log.info('%s - credentials resolved', self.__class__.__name__)
        return credentials
    
    def _update_credentials(self, credentials: Credentials, secret_key: str):
        log.info('%s - refreshing token', self.__class__.__name__)

        credentials.refresh(Request())
        updated_secret = self._extract_credential_data(credentials)
        self._secret_manager_service.update_secret(secret_key, updated_secret)
        return credentials

    def _extract_credential_data(self, credentials: Credentials) -> dict:
        log.info('%s - extracting credentials data', self.__class__.__name__)

        return {
            GoogleCalendarCredentialsConsts.ACCESS_TOKEN: credentials.token,
            GoogleCalendarCredentialsConsts.REFRESH_TOKEN: credentials.refresh_token,
            GoogleCalendarCredentialsConsts.CLIENT_ID: credentials.client_id,
            GoogleCalendarCredentialsConsts.CLIENT_SECRET: credentials.client_secret
        }