from datetime import time

from gcsa.event import EmailReminder, Event, PopupReminder

from src.main.infra.utils.log_utils import log
from src.main.domain.event_model import EventDTO
from src.main.business.template.template_i import TemplateBuilderI


class GoogleCalendarTemplateBuilderImpl(TemplateBuilderI):
    def __init__(self, event_model: EventDTO):
        self.event_model: EventDTO = event_model
        log.info('Construtor - %s', self)

    def __str__(self):
        return f"{self.__class__.__name__}(event_model={self.event_model})"


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