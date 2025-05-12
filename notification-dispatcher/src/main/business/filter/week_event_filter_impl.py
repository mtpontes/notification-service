from src.main.infra.utils.log_utils import log
from src.main.domain.event_model import EventDTO
from src.main.infra.constants.constants import NumberConstants
from src.main.business.filter.event_filter_i import EventFilterI


class WeekEventFilterImpl(EventFilterI):
    def filter_events(self, events: list[EventDTO]) -> list[EventDTO]:
        log.info('%s - input: %s', self.__class__.__name__, events)

        filtered_events = []
        for event in events:
            days_to_expire = event.get_remaining_time().days
            if days_to_expire >= NumberConstants.ZERO and days_to_expire <= NumberConstants.SEVEN:
                filtered_events.append(event)

        filtered_events = sorted(filtered_events, key=lambda event: event.dt_end)
        
        log.info('%s - output: %s', self.__class__.__name__, filtered_events)
        return filtered_events