from abc import ABC,abstractmethod

########################## ABSTRACT METHOD #########################################
"""
class Car(ABC):
    
    @abstractmethod
    def color(self):
        pass
    
    @abstractmethod
    def company(self):
        pass
    
    def wheels(self):  #------------> abstract class must have one or many concrete methods
        print("I have four wheels (Concrete method)")

class Maruti(Car):
    
    def color(self):
        print("My color is white")
        
    def company(self):
        print("Suzuki company")
        
             
obj=Maruti()
obj.color()
obj.company()
obj.wheels()
"""     
################################### INTERFACE ############################

class Car(ABC):

    @abstractmethod
    def color(self):
        pass
    
    @abstractmethod
    def company(self):
        pass  
        
    @classmethod
    @abstractmethod
    def wheels(cls):
        pass
        
    @staticmethod
    @abstractmethod
    def airBagSupport(stat):
        pass

class Maruti(Car):
    
    wheel=4
    
    def color(self):
        print("My color is red")
        
    def company(self):
        print("Suzuki company")
    
    @classmethod
    def wheels(cls):
        print(f"I have {cls.wheel} wheels")
        
    @staticmethod
    def airBagSupport(stat):
        if stat:
            print("I have air bags")
        else:
            print("I don't have air bags")



obj=Maruti()
obj.color()
obj.company()
Maruti.wheels()
Maruti.airBagSupport(False)