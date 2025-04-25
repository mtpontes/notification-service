import requests

from src.main.infra.utils.log_utils import log
from src.main.infra.config.app_config import AppConfig
from src.main.domain.models.user_model import UserModel
from src.main.domain.models.event_model import EventModel
from src.main.business.service.event_service import EventService
from src.main.business.notification.templates.template_i import TemplateBuilderI
from src.main.business.notification.provider.notification_provider_i import NotificationProviderI
from src.main.business.notification.templates.whatsapp_template_builder_impl import WhatsappTemplateBuilder


class WhatsappNotificationProviderImpl(NotificationProviderI):
    def __init__(self):
        self._client = requests
        self._api_token = AppConfig.whatsapp.api_token
        self._event_service = EventService()
        log.info('Constructor - %s', self)

    def __str__(self):
        token_preview = f"{self._api_token[:4]}***" if self._api_token else "None"
        return (
            f"{self.__class__.__name__}"
            f"(api_token='{token_preview}', "
            f"event_service={self._event_service.__class__.__name__})"
        )

    def notify(self, events: list[EventModel], user: UserModel) -> None:
        log.info('%s - notify input: %s', self.__class__.__name__, events)

        events_month: list[EventModel] = self._event_service.filter_month(events=events)
        events_week: list[EventModel] = self._event_service.filter_week(events=events)
        if len(events_week) == 0:
            log.info('%s - No events to notify', self.__class__.__name__)
            return

        template_builder: TemplateBuilderI = WhatsappTemplateBuilder(events_week, events_month, user)
        template: dict = template_builder.build_template()


        log.info('%s - sending notifications', self.__class__.__name__)
        response = self._client.post(
            url='https://graph.facebook.com/v22.0/673906565798611/messages',
            headers={'Authorization': f'Bearer {self._api_token}'},
            json=template,
            timeout=5
        )
        log.info('%s - server response: %s', self.__class__.__name__, response.json())