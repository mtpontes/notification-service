from src.main.infra.utils.log_utils import log
from src.main.domain.models.user_model import UserModel
from src.main.domain.repositories.user_repository_i import UserRepositoryI


class MongodbUserRepositoryImpl(UserRepositoryI):

    def find_all(self) -> list[UserModel]:
        users: list[UserModel] = list(UserModel.objects) # pylint: disable=no-member
        log.info('%s - [find_all] - All users: %s', self.__class__.__name__, len(users))
        return users