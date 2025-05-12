from datetime import datetime

from src.main.domain.user_model import UserDTO
from src.main.domain.event_model import EventDTO


class Mapper:
    
    def to_event_dto(self, data: dict) -> EventDTO:
        data['dt_init'] = datetime.fromisoformat(data['dt_init'])
        data['dt_end'] = datetime.fromisoformat(data['dt_end'])
        return EventDTO(**data)

    def to_event_dto_list(self, events_dict: list[dict]) -> list[EventDTO]:
        return [self.to_event_dto(event) for event in events_dict]
    
    def to_user_dto(self, data: dict) -> UserDTO:
        return UserDTO(**data)