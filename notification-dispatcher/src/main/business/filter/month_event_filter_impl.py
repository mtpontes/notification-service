from datetime import datetime

from src.main.infra.utils.log_utils import log
from src.main.domain.event_model import EventDTO
from src.main.business.filter.event_filter_i import EventFilterI


class MonthEventFilterImpl(EventFilterI):
    def filter_events(self, events: list[EventDTO]) -> list[dict]:
        log.info('%s - input: %s', self.__class__.__name__, events)
        
        filtered_events = []
        for event in events:
            current_month = datetime.now().month
            end = event.dt_end.month

            if end is current_month:
                filtered_events.append(event)
                
        filtered_events = sorted(filtered_events, key=lambda event: event.dt_end)
        log.info('%s - output: %s', self.__class__.__name__, filtered_events)
        return filtered_events
