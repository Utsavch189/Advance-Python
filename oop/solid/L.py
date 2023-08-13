"""
Liskov Substitution is , if class B is subtype of class A, then 
we should ne able to replace object of A with B without breaking the
behaviour of the program
"""
"""
subclass should extend the capability of parent class not narrow it down,
"""

from abc import ABC,abstractmethod

class Bike(ABC):
    
    @abstractmethod
    def turnOnEngine(self):
        pass

    @abstractmethod
    def accelerate(self,speed:int):
        pass

class MotorBike(Bike):

    def __init__(self) -> None:
        self.engine:bool=False
        self.speed:int=0

    def turnOnEngine(self):
        self.engine=True
    
    def accelerate(self,speed:int):
        self.speed+=speed

class Bicycle(Bike):
    def __init__(self) -> None:
        self.speed:int=0

    def turnOnEngine(self):
        raise Exception("no engine found...")
    
    def accelerate(self,speed:int):
        self.speed+=speed

if __name__=="__main__":
    m=MotorBike()
    m.turnOnEngine()
    m.accelerate(20)

    b=Bicycle()
    b.turnOnEngine() #--> will throw the error because although bicycle implement bike , but a bicycle does not have engine.
    b.accelerate(5)

"""
Here Bicycle class narrow up the capability of Bike..
so it breaks Liskov Substitution
"""

"""
Solution can be made up with Interface Segments
"""