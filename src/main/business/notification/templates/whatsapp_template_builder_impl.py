from enum import Enum
from datetime import datetime

from src.main.infra.utils.log_utils import log
from src.main.infra.utils.date_utils import DateUtils
from src.main.domain.models.user_model import UserModel
from src.main.domain.models.event_model import EventModel
from src.main.domain.constants.constants import NumberConsts, TemplateConsts
from src.main.business.notification.templates.template_i import TemplateBuilderI


class Period(Enum):
    MONTH = 30
    WEEK = 7

class WhatsappTemplateBuilder(TemplateBuilderI):
    def __init__(self, events_week: list[EventModel], events_month: list[dict], user: UserModel):
        self.events_week: list[EventModel] = events_week
        self.events_month: list[EventModel] = events_month
        self.user: UserModel = user
        log.info('Constructor - %s', self)

    def __str__(self):
        return (
            f"{self.__class__.__name__}"
            f"(user='{self.user.full_name}', "
            f"events_week_count={len(self.events_week)}, "
            f"events_month_count={len(self.events_month)})"
        )

    def build_template(self) -> object:
        log.info('%s - building template', self.__class__.__name__)
        user_name: str = self.user.full_name.split(' ')[NumberConsts.ZERO]
        user_phone: str = self.user.phone

        events_week_details: list[str] = self._format_week_events(events_week=self.events_week)
        total_events_week_formatted: int = self._format_total_period(events=self.events_week, period=Period.WEEK)
        total_events_month_formatted: int = self._format_total_period(events=self.events_month, period=Period.MONTH)

        return self._build(
            user_phone,
            user_name,
            events_week_details,
            total_events_week_formatted,
            total_events_month_formatted,
        )

    def _format_total_period(self, events: list[EventModel], period: Period) -> int:
        days_interval = period.value
        events_expiring_within_interval: list[EventModel] = []

        for event in events:
            if (event.dt_end - datetime.now()).days <= days_interval:
                events_expiring_within_interval.append(event)

        return len(events_expiring_within_interval) or NumberConsts.ZERO

    def _format_week_events(self, events_week: list[EventModel]) -> str:
        formmated_events: list[str] = []

        for events in events_week:
            formatted: str = f"• {events.title} - {DateUtils.to_date_br_str(events.dt_end)}"
            formmated_events.append(formatted)

        while len(formmated_events) < NumberConsts.TRHEE:
            formmated_events.append(TemplateConsts.NOT_APPLICABLE)

        return formmated_events[:NumberConsts.TRHEE]

    def _build(
        self,
        user_phone: str,
        user_name: str,
        events_week_details: list[EventModel],
        total_week: int,
        total_month: int,
    ) -> dict:
        log.info(
            '%s - _build method: user_phone=%s, user_name=%s, events_week_details=%s, total_week=%s, total_month=%s',
            self.__class__.__name__,
            user_phone,
            user_name,
            events_week_details,
            total_week,
            total_month,
        )
        return {
            "messaging_product": "whatsapp",
            "to": user_phone,
            "type": "template",
            "template": {
                "name": "lembrete_faculdade",
                "language": {"code": "pt_BR"},
                "components": [
                    {
                        "type": "body",
                        "parameters": [
                            {"type": "text", "parameter_name": "user_name", "text": user_name},
                            {"type": "text", "parameter_name": "ativ_prazo_1", "text": events_week_details[NumberConsts.ZERO]},
                            {"type": "text", "parameter_name": "ativ_prazo_2", "text": events_week_details[NumberConsts.ONE]},
                            {"type": "text", "parameter_name": "ativ_prazo_3", "text": events_week_details[NumberConsts.TWO]},
                            {"type": "text", "parameter_name": "qt_ativ_7_dias", "text": total_week},
                            {"type": "text", "parameter_name": "total_atividades_mes", "text": total_month},
                        ],
                    }
                ],
            },
        }