from src.main.infra.utils.log_utils import log
from src.main.domain.models.user_model import UserModel
from src.main.domain.models.event_model import EventModel
from src.main.application.dto import EventDispatcherDTO, UserDispatcherDTO


class Mapper:
    
    def to_EventOutputDTO(self, event: EventModel) -> EventDispatcherDTO:
        event_dict = event.to_mongo().to_dict()
        
        event_dict.pop('_id', None)
        event_dict.pop('user', None)
        
        event_dict['dt_init'] = str(event_dict['dt_init'])
        event_dict['dt_end'] = str(event_dict['dt_end'])

        converted = EventDispatcherDTO(**event_dict)
        log.info('%s - [to_EventOutputDTO] - Converted: %s', self.__class__.__name__, converted)
        return converted
    
    def to_EventOutputDTO_list(self, events: list[EventModel]) -> list[EventDispatcherDTO]:
        return [self.to_EventOutputDTO(event) for event in events]
    
    def to_UserDispatcherDTO(self, user: UserModel) -> UserDispatcherDTO:
        user_dict = user.to_mongo().to_dict()
        
        user_dict.pop('_id', None)
        user_dict.pop('providers', None)
        
        converted = UserDispatcherDTO(**user_dict)
        log.info('%s - [to_UserDispatcherDTO] - Converted: %s', self.__class__.__name__, converted)
        return converted