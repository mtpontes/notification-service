from enum import Enum
from datetime import datetime

from src.main.infra.utils.log_utils import log
from src.main.domain.user_model import UserDTO
from src.main.domain.event_model import EventDTO
from src.main.infra.utils.date_utils import DateUtils
from src.main.business.template.template_i import TemplateBuilderI
from src.main.infra.constants.constants import NumberConstants, TemplateConstants


class Period(Enum):
    MONTH = 30
    WEEK = 7

class WhatsappTemplateBuilder(TemplateBuilderI):
    def __init__(self, events_week: list[EventDTO], events_month: list[dict], user: UserDTO):
        self.events_week: list[EventDTO] = events_week
        self.events_month: list[EventDTO] = events_month
        self.user: UserDTO = user
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
        user_name: str = self.user.full_name.split(' ')[NumberConstants.ZERO]
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

    def _format_total_period(self, events: list[EventDTO], period: Period) -> int:
        days_interval = period.value
        events_expiring_within_interval: list[EventDTO] = []

        for event in events:
            if (event.dt_end - datetime.now()).days <= days_interval:
                events_expiring_within_interval.append(event)

        return len(events_expiring_within_interval) or NumberConstants.ZERO

    def _format_week_events(self, events_week: list[EventDTO]) -> str:
        formmated_events: list[str] = []

        for events in events_week:
            formatted: str = f"• {events.title} - {DateUtils.to_date_br_str(events.dt_end)}"
            formmated_events.append(formatted)

        while len(formmated_events) < NumberConstants.TRHEE:
            formmated_events.append(TemplateConstants.NOT_APPLICABLE)

        return formmated_events[:NumberConstants.TRHEE]

    def _build(
        self,
        user_phone: str,
        user_name: str,
        events_week_details: list[EventDTO],
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
                            {"type": "text", "parameter_name": "ativ_prazo_1", "text": events_week_details[NumberConstants.ZERO]},
                            {"type": "text", "parameter_name": "ativ_prazo_2", "text": events_week_details[NumberConstants.ONE]},
                            {"type": "text", "parameter_name": "ativ_prazo_3", "text": events_week_details[NumberConstants.TWO]},
                            {"type": "text", "parameter_name": "qt_ativ_7_dias", "text": total_week},
                            {"type": "text", "parameter_name": "total_atividades_mes", "text": total_month},
                        ],
                    }
                ],
            },
        }