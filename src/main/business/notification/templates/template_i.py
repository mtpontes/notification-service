from abc import ABC, abstractmethod

class TemplateBuilderI(ABC):  # Interface
    @abstractmethod
    def build_template(self) -> object:
        raise NotImplementedError('Required method')
