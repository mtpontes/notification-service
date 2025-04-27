from src.main.domain.models.user_model import UserModel
from src.main.domain.models.event_model import EventModel
from src.main.domain.repositories.event_repository.event_repository_i import EventRepositoryI


class MongodbEventRepositoryImpl(EventRepositoryI):

    def find_all_by_user(self, user: UserModel) -> list[EventModel]:
        return list(EventModel.objects(user=user)) # pylint: disable=no-member