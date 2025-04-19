import requests

from src.main.infra.config.app_config import AppConfig
from src.main.domain.models.user_model import UserModel
from src.main.domain.models.event_model import EventModel
from src.main.business.service.event_service import EventService
from src.main.business.notification.templates.template_i import TemplateBuilderI
from src.main.business.notification.provider.notification_provider_i import NotificationProviderI
from src.main.business.notification.templates.whatsapp_template_utils import WhatsappTemplateBuilder


class WhatsappNotificationProviderImpl(NotificationProviderI):
    def __init__(self):
        self.client = requests
        self.api_token = AppConfig.whatsapp.api_token
        self.event_service = EventService()

    def notify(self, events: list[EventModel], user: UserModel) -> None:
        events_week: list[EventModel] = self.event_service.filter_week(events=events)
        if len(events_week) == 0: 
            return

        events_month: list[EventModel] = self.event_service.filter_month(events=events)
        
        template_builder: TemplateBuilderI = WhatsappTemplateBuilder(events_week, events_month, user)
        template: dict = template_builder.build_template()

        response = self.client.post(
            url='https://graph.facebook.com/v22.0/673906565798611/messages',
            headers={'Authorization': f'Bearer {self.api_token}'},
            json=template,
            timeout=5
        )
        print(response.json())