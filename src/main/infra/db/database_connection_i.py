from abc import abstractmethod, ABC

class DataConnectionI(ABC):
    @abstractmethod
    def connect(self):
        pass