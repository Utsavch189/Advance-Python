"""
Abstract Factory Method is a Creational Design pattern that allows you to produce the families of related objects without 
specifying their concrete classes. Using the abstract factory method, we have the easiest ways to produce a similar type 
of many objects. 
It provides a way to encapsulate a group of individual factories. 
Basically, here we try to abstract the creation of the objects depending on the logic, business, platform choice, etc.
"""
class YammahaFactory:
    def __init__(self,bike_obj:object) -> None:
        self.bike_obj:object=bike_obj
    
    def bike_desc(self):
        bike:object=self.bike_obj
        print("name of the bike : ",bike.__str__())
        print("price :",bike.price())

class YamahaR15:

    def __str__(self) -> str:
        return "Yamaha R15 V4"
    
    def price(self)->str:
        return "1,82,556"

class YamahaMT15:

    def __str__(self) -> str:
        return "Yamaha MT 15"

    def price(self)->str:
        return "1,68,208"

class YamahaFZ:

    def __str__(self) -> str:
        return "Yamaha FZ S FI"
    
    def price(self)->str:
        return "1,21,979"

from enum import Enum

class Bikes(Enum):
    YamahaR15=YammahaFactory(YamahaR15())
    YamahaMT15=YammahaFactory(YamahaMT15())
    YamahaFZ=YammahaFactory(YamahaFZ())


if __name__=="__main__":
    print("Bikes are availabe in our factory are : YamahaR15 , YamahaMT15 ,YamahaFZ")
    name=str(input("Enter your bike : "))
    obj=Bikes[name].value
    obj.bike_desc()
