"""
Interfaces should be such, that childs should not implement
unnecessary methods they do not need,
"""

"""
According to our prev example of Bike,
"""
from abc import ABC,abstractmethod

################################
# Interface Segmentation
class BikesWithEngine(ABC):
    @abstractmethod
    def turnOnEngine(self):
        pass

    @abstractmethod
    def accelerate(self,speed:int):
        pass

class BikesWithoutEngine(ABC):

    @abstractmethod
    def accelerate(self,speed:int):
        pass
################################
class MotorBike(BikesWithEngine):

    def __init__(self) -> None:
        self.engine:bool=False
        self.speed:int=0

    def turnOnEngine(self):
        self.engine=True
    
    def accelerate(self,speed:int):
        self.speed+=speed

class Bicycle(BikesWithoutEngine):
    def __init__(self) -> None:
        self.speed:int=0
    
    def accelerate(self,speed:int):
        self.speed+=speed

if __name__=="__main__":
    m=MotorBike()
    m.turnOnEngine()
    m.accelerate(20)

    b=Bicycle()
    b.accelerate(5)