from typing import Protocol,Any,List
from abc import ABC,abstractmethod

class Observer(Protocol):

    @abstractmethod
    def weather_update(self):...