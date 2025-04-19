from src.main.infra.utils.date_utils import DateUtils
from src.main.domain.models.user_model import UserModel
from src.main.domain.models.event_model import EventModel
from src.main.domain.constants.constants import EventConstants


class EventRepository:
    def create_event(self, data: dict, user: UserModel) -> EventModel:
        event = EventModel(
            title=data[EventConstants.TITLE],
            description=data[EventConstants.DESCRIPTION],
            dt_init=DateUtils.to_datetime(data[EventConstants.DT_INIT]),
            dt_end=DateUtils.to_datetime(data[EventConstants.DT_END]),
            user=user
        )
        event.save()
        return event

    def get_all_by_user(self, user: UserModel) -> list[EventModel]:
        return list(EventModel.objects(user=user)) # pylint: disable=no-member