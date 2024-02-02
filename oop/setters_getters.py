class Myclass:

          def __init__(self,name:str,age:int) -> None:
                  self.__name=name
                  self.age=age

          @property
          def Name(self)->str:
                  return self.__name
          
          def Age(self)->int:
                  return self.age
          
          def setAge(self,age:int)->None:
                  self.age=age
          
          @Name.setter
          def Name(self,name:str)->None:
                 self.__name=name 

c=Myclass("Utsav",22)
print(c.Name)
print(c.Age())

c.Name="Ram"
c.setAge(50)
print(c.Name)
print(c.Age())
print(c.age)
print(c.__name)