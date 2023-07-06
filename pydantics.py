from pydantic import BaseModel,validator,constr,conint

class Person(BaseModel):
    firstname:constr(min_length=5)=None
    lastname:str=None
    #age:int=None
    age:conint(gt=18)=None
    
    """
    @validator('age')
    def check_age(cls,value):
        if value<18:
            raise ValueError("Can't allow")
        return value
    """
    
    @validator('firstname')
    def cap_firstname(cls,value):
        return value.strip().capitalize()

try:
    P=Person(firstname="Utsav",lastname="Chatterjee",age=17)
    print(p)
except Exception as e:
    print(e)
p=Person(firstname="utsav",lastname="Chatterjee",age=22)
print(p.age)
print(p)

