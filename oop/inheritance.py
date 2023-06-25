
############### SINGLE INHERITANCE ######################
class Animal:

    def __init__(self, name:str,age:int):
        self.name=name
        self.age=age

    def getName(self)->str:
        print(self.name)
    
    def getAge(self)->int:
        print(self.age)
    
class Monkey(Animal):

    def __init__(self,name:str,age:int):
        super().__init__(name,age)


############### MULTILEVEL INHERITANCE ######################
class Animal:

    def __init__(self, name:str,age:int):
        self.name=name
        self.age=age

    def getName(self)->str:
        print(self.name)
    
    def getAge(self)->int:
        print(self.age)

class Monkey(Animal):

    def __init__(self,name:str,age:int,types:str):
        super().__init__(name,age)
        self.types=types
    
    def getType(self):
        print(self.types)

class Human(Monkey):

    def __init__(self,name:str,age:int,types:str,nationality:str):
        super().__init__(name,age,types)
        self.nationality=nationality

    def getNationality(self):
        print(self.nationality)

############### MULTIPLE INHERITANCE ######################
class A:

    def eat(self):
        print("I can eat...")

class B:

    def speak(self):
        print("I can speak...")

class C(A,B):

    def walk(self):
        print("I can walk also...")

if __name__=="__main__":
    #m=Monkey(name="John",age=5)
    #m.getName()
    #m.getAge()

    #h=Human("utsav",22,"human","Indian")
    #h.getName()
    #h.getAge()
    #h.getType()
    #h.getNationality()

    c=C()
    c.eat()
    c.speak()
    c.walk()

