from src.main.domain.models.user_model import UserModel
from src.main.domain.repositories.user_repository.user_repository_i import UserRepositoryI


class MongodbUserRepositoryImpl(UserRepositoryI):

    def find_all(self) -> list[UserModel]:
        return list(UserModel.objects) # pylint: disable=no-member