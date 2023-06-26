"""

class A:
    def __init__(self,name:str,age:int):
        self.name=name
        self.age=age

a=A("Utsav",22)
print(a.__dict__)
a.address="Guptipara" #-------> Although the class accepts only name and age, but because of dynamic nature extra attributes should be added.Which may cause performance decrease.
print(a.__dict__)
"""

class A:
    __slots__="name","age"
    def __init__(self,name:str,age:int):
        self.name=name
        self.age=age
    

a=A("Utsav",22)
a.address="Guptipara" #----------> Now we can't add any attribute dynamically except name and age due to slots.
