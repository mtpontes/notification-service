from enum import Enum
from datetime import datetime

from src.main.infra.utils.date_utils import DateUtils
from src.main.domain.constants.constants import Consts
from src.main.domain.models.user_model import UserModel
from src.main.domain.models.event_model import EventModel
from src.main.business.notification.templates.template_i import TemplateBuilderI


class Period(Enum):
    MONTH = 30
    WEEK = 7

class WhatsappTemplateBuilder(TemplateBuilderI):
    def __init__(self, events_week: list[EventModel], events_month: list[dict], user: UserModel):
        self.events_week: list[EventModel] = events_week
        self.events_month: list[EventModel] = events_month
        self.user: UserModel = user

    def build_template(self) -> object:
        user_name: str = self.user.full_name.split(' ')[0]
        user_phone: str = self.user.phone

        events_week_details: list[str] = self.__format_week_events(events_week=self.events_week)
        total_events_week_formatted: int = self.__format_total_period(events=self.events_week, period=Period.WEEK)
        total_events_month_formatted: int = self.__format_total_period(events=self.events_month, period=Period.MONTH)

        return self.__build(
            user_phone,
            user_name,
            events_week_details,
            total_events_week_formatted,
            total_events_month_formatted,
        )

    def __format_total_period(self, events: list[EventModel], period: Period) -> int:
        days_interval = period.value
        events_expiring_within_interval: list[EventModel] = []

        for event in events:
            if (event.dt_end - datetime.now()).days <= days_interval:
                events_expiring_within_interval.append(event)

        return len(events_expiring_within_interval) or 0

    def __format_week_events(self, events_week: list[EventModel]) -> str:
        formmated_events: list[str] = []

        for events in events_week:
            formatted: str = f"• {events.title} - {DateUtils.to_date_br_str(events.dt_end)}"
            formmated_events.append(formatted)

        while len(formmated_events) < Consts.NUMBER_TRHEE:
            formmated_events.append(Consts.NOT_APPLICABLE)

        return formmated_events[:3]

    def __build(
        self,
        user_phone: str,
        user_name: str,
        events_week_details: list[EventModel],
        total_week: int,
        total_month: int,
    ) -> dict:
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
                            {"type": "text", "parameter_name": "user_name", "text": user_name},                 # Nome do usuário
                            {"type": "text", "parameter_name": "ativ_prazo_1", "text": events_week_details[0]}, # Resumo das atividades
                            {"type": "text", "parameter_name": "ativ_prazo_2", "text": events_week_details[1]},
                            {"type": "text", "parameter_name": "ativ_prazo_3", "text": events_week_details[2]},
                            {"type": "text", "parameter_name": "qt_ativ_7_dias", "text": total_week},           # Total em 7 dias
                            {"type": "text", "parameter_name": "total_atividades_mes", "text": total_month},    # Total no mês
                        ],
                    }
                ],
            },
        }
