from observer.main import Observer
from observable.weatherstation_observable import WeatherStationObservable

class Mobile(Observer):


    def weather_update(self,inst):
        print("In Mobile : ",inst.gets())
        return inst.gets()

class TV(Observer):


    def weather_update(self,inst):
        print("In TV : ",inst.gets())
        return inst.gets()

if __name__=="__main__":
    obervable=WeatherStationObservable()
    
    mobile=Mobile()
    tv=TV()

    obervable.add(mobile)
    obervable.add(tv)

    obervable.sets(27.3)

    obervable.remove(tv)
    
    obervable.sets(28.3)

    obervable.sets(28.3) # as our business logic same temp update should not be notified
