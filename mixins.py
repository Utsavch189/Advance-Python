"""
A mixin is a special kind of multiple inheritance. There are two main situations where mixins are used:

1. You want to provide a lot of optional features for a class.
2. You want to use one particular feature in a lot of different classe
"""

# Let's Consider a Base Class Shape:
from typing import Union

class Shape:

    def __init__(self,a:Union[int,float]=None,b:Union[int,float]=None) -> None:
        self.a=a
        self.b=b

    def area(self,shape_type:str=None)->Union[int,float]:
        if shape_type.lower()=='triangle':
            return 0.5*(self.a*self.b)
        elif shape_type.lower()=='square':
            return self.a**2
        elif shape_type.lower()=='circle':
            return 3.14*(self.a**2)

# Let's consider a Child Class Circle:

class Circle(Shape):

    def __init__(self, a: int | float = None, b: int | float = None) -> None:
        super().__init__(a, b)
    
    def area(self) -> int | float:
        return super().area("circle")

c=Circle(5)
print(c.area())

"""
But now what happen that I want to add a serializer,

1. I can't add it only Circle Class bcz other shapes also may need this feature

2. I can add it in Shape Class but it breaks single responsibility rule and more than that if other Child Classes
    which are not child of Shape Class , if they need serialization then I can't provide it bcz the feature is injected
    in Shape Class only.

3. So I can make a generic Serializer Class To serialize the result only, and this is the mixin here.
"""

class SerializerMixin:

    def __init__(self,result:Union[int,float]) -> None:
        self.result=result
    
    def serialize(self):
        return {
            "result":self.result
        }

class Shape:

    def __init__(self,a:Union[int,float]=None,b:Union[int,float]=None) -> None:
        self.a=a
        self.b=b

    def area(self,shape_type:str=None)->Union[int,float]:
        if shape_type.lower()=='triangle':
            return 0.5*(self.a*self.b)
        elif shape_type.lower()=='square':
            return self.a**2
        elif shape_type.lower()=='circle':
            return 3.14*(self.a**2)

class Circle(Shape,SerializerMixin):

    def __init__(self, a: int | float = None, b: int | float = None) -> None:
        super().__init__(a, b)
    
    def area(self) -> int | float:
        self.result=super().area("circle")
        return self.result

    def serialize(self):
        return SerializerMixin(self.result).serialize()

c=Circle(5)
print(c.area())
print(c.serialize())

c1=Circle(9)
print(c1.area())
print(c1.serialize())