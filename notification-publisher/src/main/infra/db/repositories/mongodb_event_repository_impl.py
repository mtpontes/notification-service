from datetime import datetime

from src.main.infra.utils.log_utils import log
from src.main.domain.models.event_model import EventModel
from src.main.domain.repositories.event_repository_i import EventRepositoryI


class MongodbEventRepositoryImpl(EventRepositoryI):

    def find_all_by_user(self, user_id: str) -> list[EventModel]:
        events: list[EventModel] = list(EventModel.objects(user=user_id, dt_end__gte=datetime.now())) # pylint: disable=no-member
        log.info('%s - [find_all_by_user] - All events: %s', self.__class__.__name__, len(events))

        return events