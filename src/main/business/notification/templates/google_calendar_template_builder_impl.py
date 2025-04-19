from datetime import time

from gcsa.event import EmailReminder, Event, PopupReminder

from src.main.domain.models.event_model import EventModel
from src.main.business.notification.templates.template_i import TemplateBuilderI


class GoogleCalendarTemplateBuilderImpl(TemplateBuilderI):
    def __init__(self, event_model: EventModel):
        self.event_model = event_model
    
    def build_template(self) -> object:
        return Event(
            summary=self.event_model.title,
            start=self.event_model.dt_end,
            reminders=[
                EmailReminder(days_before=7, at=time(0, 0)),
                PopupReminder(days_before=3, at=time(0, 0)),
                PopupReminder(minutes_before_start=360),
                PopupReminder(minutes_before_start=720),
                PopupReminder(minutes_before_start=1080),
            ]
        )