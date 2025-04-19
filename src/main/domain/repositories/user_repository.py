from src.main.domain.models.user_model import UserModel


class UserRepository():
    def create_user(self, complete_name: str, email: str, phone: str) -> UserModel:
        user = UserModel(complete_name=complete_name, email=email, phone=phone)
        user.save()
        return user

    def get_by_email(self, email: str) -> UserModel:
        return UserModel.objects(email=email).first() # pylint: disable=no-member

    def get_all_users(self) -> list[UserModel]:
        return list(UserModel.objects) # pylint: disable=no-member