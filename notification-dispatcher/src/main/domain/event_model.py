from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class EventDTO:
    title: str
    description: str
    dt_init: datetime
    dt_end: datetime

    def get_remaining_time(self) -> timedelta:
        return self.dt_end - datetime.now()