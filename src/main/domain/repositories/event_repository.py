from src.main.domain.models.user_model import UserModel
from src.main.domain.models.event_model import EventModel


class EventRepository:

    def get_all_by_user(self, user: UserModel) -> list[EventModel]:
        return list(EventModel.objects(user=user)) # pylint: disable=no-member