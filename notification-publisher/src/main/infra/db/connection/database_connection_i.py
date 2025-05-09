from abc import abstractmethod, ABC


class DatabaseConnectionI(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def close(self):
        pass