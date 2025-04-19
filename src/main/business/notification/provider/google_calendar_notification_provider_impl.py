from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from google.oauth2.credentials import Credentials

from src.main.infra.integration.google_credential_manager import GoogleCredentialManager
from src.main.domain.models.user_model import UserModel
from src.main.domain.models.event_model import EventModel
from src.main.business.notification.templates.template_i import TemplateBuilderI
from src.main.business.notification.provider.notification_provider_i import NotificationProviderI
from src.main.business.notification.templates.google_calendar_template_builder_impl import (
    GoogleCalendarTemplateBuilderImpl,
)


class GoogleCalendarNotificationProviderImpl(NotificationProviderI):
    def __init__(self):
        self.__google_calendar_client: GoogleCalendar = None
        self.__google_credential_manager: GoogleCredentialManager = GoogleCredentialManager()

    def notify(self, events: list[EventModel], user: UserModel) -> None:
        secret_key = user.complete_name
        
        credentials: Credentials = self.__google_credential_manager.get_valid_credentials(secret_key=secret_key)
        self.__google_calendar_client = GoogleCalendar(credentials=credentials)
        
        new_event_models: list[EventModel] = self.__remove_existing_calendar_events(event_models=events)
        for event_model in new_event_models:
            template_builder: TemplateBuilderI = GoogleCalendarTemplateBuilderImpl(event_model=event_model)
            event: Event = template_builder.build_template()
            self.__google_calendar_client.add_event(event=event)
        
    def __remove_existing_calendar_events(self, event_models: list[EventModel]) -> list[EventModel]:
        new_events = []
        
        for event_model in event_models:
            event_exists = False

            for event in self.__google_calendar_client:
                if event.summary == event_model.title:
                    event_exists = True
                    break

                if not event_exists:
                    print(f'Event name: {event.summary}, EventModel name: {event_model.title}')
                    new_events.append(event_model)

        return new_events
