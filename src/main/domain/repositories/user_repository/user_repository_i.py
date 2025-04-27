from abc import ABC, abstractmethod

from src.main.domain.models.user_model import UserModel


class UserRepositoryI(ABC):

    @abstractmethod
    def find_all(self) -> list[UserModel]:
        raise NotImplementedError('Required method')
