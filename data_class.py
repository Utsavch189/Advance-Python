from dataclasses import dataclass,field
import random

def rand()->int:
    return random.randint(0,99)

@dataclass(frozen=True) #-----> slots=True means it will not allow extra attributes and frozen=True means after initialize values of a instance we can't update for that
class Person:
    name:str
    age:int
    id1:int=rand() #------> this type of default initialize will give the same value for the all instances
    id:int=field(default_factory=rand) #-----------> this type of default initialize will give the different value for the all instances 
    
p=Person(name="utsav",age=22)
p1=Person(name="supu",age=21)

print(p)
print(p1)

data={
    "name":"abc",
    "age":12
}
p2=Person(**data)
print(p2)


@dataclass
class Rectangle:
    width: float
    height: float

    def __post_init__(self):
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Width and height must be positive numbers")
try:
    print(Rectangle(-2,55))
except Exception as e:
    print(e)

def calculate_area(width, height):
    return width * height

@dataclass
class Rectangle:
    width: int=field(default_factory=int)
    height: int=field(default_factory=int)
    area: int = field(default_factory=int)
    area_function:object=field(default_factory=object)
    def __post_init__(self):
        if self.area == 0:
            self.area = self.area_function(self.width, self.height)



rectangle = Rectangle(area_function=calculate_area)
print(rectangle.area)