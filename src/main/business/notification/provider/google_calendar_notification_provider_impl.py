from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from google.oauth2.credentials import Credentials

from src.main.infra.utils.log_utils import log
from src.main.infra.integration.google_credential_manager import GoogleCredentialManager
from src.main.domain.models.user_model import UserModel
from src.main.domain.models.event_model import EventModel
from src.main.business.notification.templates.template_i import TemplateBuilderI
from src.main.business.notification.provider.notification_provider_i import NotificationProviderI
from src.main.business.notification.templates.google_calendar_template_builder_impl import (
    GoogleCalendarTemplateBuilderImpl
)


class GoogleCalendarNotificationProviderImpl(NotificationProviderI):
    def __init__(self):
        self._google_calendar_client: GoogleCalendar = None
        self._google_credential_manager: GoogleCredentialManager = GoogleCredentialManager()
        log.info('Constructor - %s', self)

    def __str__(self):
        return (
            f"{self.__class__.__name__}"
            f"(google_calendar_client={self._google_calendar_client}, "
            f"credential_manager={self._google_credential_manager.__class__.__name__})"
        )

    def notify(self, events: list[EventModel], user: UserModel) -> None:
        log.info('%s - notify input: %s', self.__class__.__name__, events)

        secret_key = user.full_name.replace(' ', '')
        credentials: Credentials = self._google_credential_manager.get_valid_credentials(secret_key=secret_key)
        self._google_calendar_client = GoogleCalendar(credentials=credentials)
        log.info('%s - Google Calendar client connected', self.__class__.__name__)
        
        new_event_models: list[EventModel] = self._remove_existing_calendar_events(event_models=events)
        for event_model in new_event_models:
            template_builder: TemplateBuilderI = GoogleCalendarTemplateBuilderImpl(event_model=event_model)
            event: Event = template_builder.build_template()
            self._google_calendar_client.add_event(event=event)
        log.info('%s - events added', self.__class__.__name__)
        
    def _remove_existing_calendar_events(self, event_models: list[EventModel]) -> list[EventModel]:
        log.info('%s - removing existing events', self.__class__.__name__)
        new_events = []
        
        for event_model in event_models:
            event_exists = False

            for event in self._google_calendar_client:
                if event.summary == event_model.title:
                    event_exists = True
                    break

                if not event_exists:
                    print(f'Event name: {event.summary}, EventModel name: {event_model.title}')
                    new_events.append(event_model)

        log.info('%s - new events: %s', self.__class__.__name__, new_events)
        return new_events
