from .main import Obervable

class WeatherStationObservable(Obervable):

    temp=0.0
    objs=list()

    @classmethod
    def add(cls, obj: object) -> None:
        cls.objs.append(obj)

    @classmethod
    def remove(cls, obj: object) -> None:
        cls.objs.remove(obj)

    def notify(self)->None:
        for i in self.objs:
            i.weather_update(self)

    
    def setTemp(cls,temps:float):
        if cls.temp!=temps:
            cls.temp=temps
            cls.notify()


    def getTemp(cls):
        return cls.temp