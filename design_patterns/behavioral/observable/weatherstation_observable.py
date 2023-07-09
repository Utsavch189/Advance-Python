from .main import Obervable

class WeatherStationObservable(Obervable):

    _subscribers=list()

    def __init__(self) -> None:
        self._temp=0.0

    @classmethod
    def add(cls, obj: object) -> None:
        cls._subscribers.append(obj)

    @classmethod
    def remove(cls, obj: object) -> None:
        cls._subscribers.remove(obj)

    def notify(self)->None:
        for i in self._subscribers:
            i.weather_update(self)

    def sets(self,temps:float):
        if self._temp!=temps:
            self._temp=temps
            self.notify()

    def gets(self):
        return self._temp