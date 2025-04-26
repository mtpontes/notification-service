from abc import ABC, abstractmethod

from src.main.domain.models.user_model import UserModel


class UserRepository(ABC):

    @abstractmethod
    def get_all_users(self) -> list[UserModel]:
        pass