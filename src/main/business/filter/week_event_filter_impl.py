from src.main.infra.utils.log_utils import log
from src.main.domain.models.event_model import EventModel
from src.main.domain.constants.constants import NumberConsts
from src.main.business.filter.event_filter_i import EventFilterI


class WeekEventFilterImpl(EventFilterI):
    def filter_events(self, events: list[EventModel]) -> list[EventModel]:
        log.info('%s - input: %s', self.__class__.__name__, events)

        filtered_events = []
        for event in events:
            days_to_expire = event.get_remaining_time().days
            if days_to_expire >= NumberConsts.ZERO and days_to_expire <= NumberConsts.SEVEN:
                filtered_events.append(event)

        filtered_events = sorted(filtered_events, key=lambda event: event.dt_end)
        
        log.info('%s - output: %s', self.__class__.__name__, filtered_events)
        return filtered_events