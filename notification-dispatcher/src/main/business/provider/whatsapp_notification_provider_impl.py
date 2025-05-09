import requests

from src.main.infra.config.app_config import AppConfig
from src.main.infra.utils.log_utils import log
from src.main.domain.user_model import UserDTO
from src.main.domain.event_model import EventDTO
from src.main.business.service.event_service import EventService
from src.main.business.provider.notification_provider_i import NotificationProviderI
from src.main.business.template.template_i import TemplateBuilderI
from src.main.business.template.whatsapp_template_builder_impl import WhatsappTemplateBuilder


class WhatsappNotificationProviderImpl(NotificationProviderI):
    def __init__(self):
        self._client = requests
        self._api_token = AppConfig.whatsapp.api_token
        self._event_service = EventService()
        log.info('Constructor - %s', self)

    def __str__(self):
        return (
            f"{self.__class__.__name__}"
            f"(api_token='{self._api_token[:4]}', "
            f"event_service={self._event_service.__class__.__name__})"
        )

    def notify(self, events: list[EventDTO], user: UserDTO) -> None:
        log.info('%s - notify input: %s', self.__class__.__name__, events)

        events_month: list[EventDTO] = self._event_service.filter_month(events=events)
        events_week: list[EventDTO] = self._event_service.filter_week(events=events)
        if len(events_week) == 0:
            log.info('%s - No events to notify', self.__class__.__name__)
            return

        template_builder: TemplateBuilderI = WhatsappTemplateBuilder(events_week, events_month, user)
        template: dict = template_builder.build_template()

        log.info('%s - final template: %s', self.__class__.__name__, template)
        response = self._client.post(
            url='https://graph.facebook.com/v22.0/673906565798611/messages',
            headers={'Authorization': f'Bearer {self._api_token}',  'User-Agent': 'python-requests/2.31.0'},
            json=template,
            timeout=5
        )
        log.info('%s - server response: %s', self.__class__.__name__, response.json())