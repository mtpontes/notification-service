from src.main.domain.models.user_model import UserModel


class UserRepository():

    def get_all_users(self) -> list[UserModel]:
        return list(UserModel.objects) # pylint: disable=no-member