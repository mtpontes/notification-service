from datetime import datetime

from src.main.domain.models.event_model import EventModel
from src.main.business.filter.event_filter_i import EventFilterI


class MonthEventFilterImpl(EventFilterI):
    def filter_events(self, events: list[EventModel]) -> list[dict]:
        filtered_events = []
        for event in events:
            current_month = datetime.now().month
            start = event.dt_init.month
            end = event.dt_end.month

            if start is current_month or end is current_month:
                filtered_events.append(event)
                
        filtered_events = sorted(filtered_events, key=lambda event: event.dt_fim)
        return filtered_events
