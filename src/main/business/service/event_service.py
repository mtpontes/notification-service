from src.main.business.filter.event_filter_i import EventFilterI
from src.main.business.filter.week_event_filter_impl import WeekEventFilterImpl
from src.main.business.filter.month_event_filter_impl import MonthEventFilterImpl


class EventService:
    def __init__(self):
        self.__filter_week: EventFilterI = WeekEventFilterImpl()
        self.__filter_month: EventFilterI = MonthEventFilterImpl()

    def filter_week(self, events: list[dict]) -> list[dict]:
        return self.__filter_week.filter_events(events)
    
    def filter_month(self, events: list[dict]) -> list[dict]:
        return self.__filter_month.filter_events(events)

