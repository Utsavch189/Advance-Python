from pydantic import BaseModel,validator,constr,conint

class Person(BaseModel):
    firstname:constr(min_length=1,max_length=50,strip_whitespace=True)=None
    lastname:constr(min_length=1,max_length=50,strip_whitespace=True)=None
    #age:int=None
    age:conint(ge=18)=None
    
    """
    @validator('age')
    def check_age(cls,value):
        if value<18:
            raise ValueError("Can't allow")
        return value
    """
    

    @validator('firstname','lastname')
    def cap_firstname(cls,value):
        return value.strip().capitalize()


#1.
try:
    p1=Person(firstname="ut",lastname="ch",age=18)
    print(p1)
except Exception as e:
    print(e)

#2.
p2=Person(firstname="utsav",lastname="Chatterjee",age=22)
print(p2.age)
print(p2)

#3.
data={
    "firstname":"Supratim",
    "lastname":"Majumder",
    "age":"25"
}
p3=Person(**data)
print(p3)

################## Part 2 ################################################

"""
Add Dynamic values...
"""
from random import randint

class Student(BaseModel):
    firstname:constr(min_length=1,max_length=50,strip_whitespace=True)
    lastname:constr(min_length=1,max_length=50,strip_whitespace=True)
    s_id:constr(min_length=1,max_length=20)=None
    phone:conint()=None
    password:constr(min_length=1,max_length=50,strip_whitespace=True)=None
    cpassword:constr(min_length=1,max_length=50,strip_whitespace=True)=None

    @validator('s_id',always=True)
    def set_sid(cls,value,values):

        if not value: #------------> indicates s_id value
            firstname=values['firstname']
            return firstname+str(randint(100,999))
    
    @validator('cpassword',always=True)
    def password_validate(cls,value,values):
        if value:
            password=values['password']
            if value==password:
                return value
            else:
                raise ValueError("Passwords are mismatch")
    
    @validator('phone')
    def phone_val(cls,value):
        if value:
            return str(value)

data2={
    "firstname":"Supratim Kumar",
    "lastname":"Majumder",
    "password":"1234",
    "cpassword":"1234",
    "phone":555
}
s=Student(**data2)
print(type(s.phone))

