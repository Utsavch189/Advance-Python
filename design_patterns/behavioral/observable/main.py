from typing import Protocol
from abc import abstractmethod

class Obervable(Protocol):

    @classmethod
    @abstractmethod
    def add(cls,obj)->None:...

    @classmethod
    @abstractmethod
    def remove(cls,obj)->None:...

    @abstractmethod
    def notify(self)->None:...

    @abstractmethod
    def sets(self,temps:float)->None:...

    @abstractmethod
    def gets(self)->float:...