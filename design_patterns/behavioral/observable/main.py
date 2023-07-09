from typing import Protocol
from abc import abstractmethod

class Obervable(Protocol):

    @classmethod
    @abstractmethod
    def add(cls,obj)->None:...

    @classmethod
    @abstractmethod
    def remove(cls,obj)->None:...

   
    def notify(self)->None:...

    @classmethod
    def setData(cls,temps:float)->None:...

    @classmethod
    def getData(cls)->float:...