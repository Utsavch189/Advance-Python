from dataclasses import dataclass,field
import random

def rand()->int:
    return random.randint(0,99)

@dataclass(slots=True,frozen=True) #-----> slots=True means it will not allow extra attributes and frozen=True means after initialize values of a instance we can't update for that
class Person:
    name:str
    age:int
    id1:int=rand() #------> this type of default initialize will give the same value for the all instances
    id:int=field(default_factory=rand) #-----------> this type of default initialize will give the different value for the all instances 
    
p=Person(name="utsav",age=22)
p1=Person(name="supu",age=21)

print(p)
print(p1)