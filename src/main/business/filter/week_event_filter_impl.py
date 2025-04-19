from src.main.domain.constants.constants import Consts
from src.main.domain.models.event_model import EventModel
from src.main.business.filter.event_filter_i import EventFilterI


class WeekEventFilterImpl(EventFilterI):
    def filter_events(self, events: list[EventModel]) -> list[EventModel]:
        filtered_events = []
        for event in events:
            days_to_expire = event.get_remaining_time().days
            if days_to_expire >= Consts.NUMBER_ZERO and days_to_expire <= Consts.NUMBER_SEVEN:
                filtered_events.append(event)

        filtered_events = sorted(filtered_events, key=lambda event: event.dt_fim)
        return filtered_events