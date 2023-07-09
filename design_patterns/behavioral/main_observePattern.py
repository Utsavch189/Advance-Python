from observer.main import Observer
from observable.weatherstation_observable import WeatherStationObservable

class Mobile(Observer):


    def weather_update(self,inst):
        print("In Mobile : ",inst.getTemp())
        return inst.getTemp()

class TV(Observer):


    def weather_update(self,inst):
        print("In TV : ",inst.getTemp())
        return inst.getTemp()

if __name__=="__main__":
    obervable=WeatherStationObservable()
    mobile=Mobile()
    tv=TV()

    obervable.add(mobile)
    obervable.add(tv)

    obervable.setTemp(27.3)

    obervable.remove(mobile)
    obervable.setTemp(28.3)
