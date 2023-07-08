from abc import ABC,abstractmethod

################ WITHOUT STRATEGY PATTERN #####################

"""
IF WE NOTICE BELOW EXAMPLE ALL CARS ARE THE CHILD OF Vehicle CLASS. BUT OffRoadCar AND RacingCar HAS THEIR 
NEEDED special_drive METHOD, WHICH ARE CAUSE OF CODE DUPLICATION.
"""

"""
class Vehicle(ABC):
    
    @abstractmethod
    def drive(self):
        pass

class PassengerCar(Vehicle):

    def drive(self):
        print("I have simple drive")


class OffRoadCar(Vehicle):
    
    def special_drive(self):
        print("I need a special_drive")
    
    def drive(self):
        return self.special_drive()

class RacingCar(Vehicle):
    
    def special_drive(self):
        print("I need a special_drive")
    
    def drive(self):
        return self.special_drive()

if __name__=="__main__":
    ps=PassengerCar()
    ofc=OffRoadCar()
    rc=RacingCar()
    
    ps.drive()
    ofc.drive()
    rc.drive()
"""
    
################ WITH STRATEGY PATTERN #####################
from typing import Protocol

class Drive(Protocol):

    def drive(self):
        ...
      
    def special_drive(self):
        ...
        
class Vehicle(ABC,Drive):
    
    @abstractmethod
    def fuel(self):
        pass
        

class PassengerCar(Vehicle):

    def drive(self):
        print("I have simple drive")
        
    def fuel(self):
        print("I need desel")


class OffRoadCar(Vehicle):
    
    def special_drive(self):
        print("I have a special_drive")
        
    def fuel(self):
        print("I need desel")
    

class RacingCar(Vehicle):
    
    def special_drive(self):
        print("I have a special_drive")
        
    def fuel(self):
        print("I need nitro")

if __name__=="__main__":
    ps=PassengerCar()
    ofc=OffRoadCar()
    rc=RacingCar()
    
    ps.drive()
    ofc.special_drive()
    rc.special_drive()