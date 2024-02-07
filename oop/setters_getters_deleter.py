class Myclass:

        def __init__(self,name:str) -> None:
                self.__name=name

        @property
        def Name(self)->str:
                return self.__name
        
        @Name.setter
        def Name(self,name:str)->None:
               self.__name=name 
        
        
        
        @Name.deleter
        def Name(self)->None:
               self.__name=""
        

c=Myclass("Utsav")
print(c.Name)

c.Name="Ram"

print(c.Name)

#print(c.__name)

del c.Name
print("after delete : ",c.Name)