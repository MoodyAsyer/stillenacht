from abc import ABC, abstractmethod


class Abstract(ABC):

    @abstractmethod
    def draw(self, screen):
        pass
