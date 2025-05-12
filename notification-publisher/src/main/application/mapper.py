from src.main.infra.utils.log_utils import log
from src.main.domain.models.user_model import UserModel
from src.main.domain.models.event_model import EventModel
from src.main.application.dto import EventDispatcherDTO, UserDispatcherDTO
from src.main.domain.constants.constants import EventModelConsts, UserModelConsts


class Mapper:
    
    def to_EventOutputDTO(self, event: EventModel) -> EventDispatcherDTO:
        event_dict = event.to_mongo().to_dict()
        
        event_dict.pop(EventModelConsts.ID, None)
        event_dict.pop(EventModelConsts.USER, None)
        
        event_dict[EventModelConsts.DT_INIT] = str(event_dict[EventModelConsts.DT_INIT])
        event_dict[EventModelConsts.DT_END] = str(event_dict[EventModelConsts.DT_END])

        converted = EventDispatcherDTO(**event_dict)
        log.info('%s - [to_EventOutputDTO] - Converted: %s', self.__class__.__name__, converted)
        return converted
    
    def to_EventOutputDTO_list(self, events: list[EventModel]) -> list[EventDispatcherDTO]:
        return [self.to_EventOutputDTO(event) for event in events]
    
    def to_UserDispatcherDTO(self, user: UserModel) -> UserDispatcherDTO:
        user_dict = user.to_mongo().to_dict()
        
        user_dict.pop(UserModelConsts.ID, None)
        user_dict.pop(UserModelConsts.PROVIDERS, None)
        
        converted = UserDispatcherDTO(**user_dict)
        log.info('%s - [to_UserDispatcherDTO] - Converted: %s', self.__class__.__name__, converted)
        return converted