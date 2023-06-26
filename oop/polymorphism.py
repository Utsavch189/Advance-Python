########### DUCK TYPING #########33
"""
A DUCK IS A DUCK WHICH CAN : QUACK,WALK,SWIM
"""

class A:

    def execute(self,obj):
        return obj.process()
        
class Method1:

    def process(self):
        return"processing..."
        
class Method2:

    def run(self):
        return "running..."
        
"""        
a=A()
m1=Method1()
m2=Method2()

print(a.execute(m1)) #-----> m1 is the obj here which will be accepted by a.execute() because it has process method.
print(a.execute(m2)) #------> It's not that duck because it has no process method.
"""

################ OPERATOR OVERLOAD ########################
"""
in pyhton data types like int,str,float etc all are object(built in).

whenever we do,
    a=5
    b=6
    c=a+b
behind the scene the '+' operator overloads with the __add__() method of int.

c=a+b=int.__add__(a,b)

there has all kind of special attributes like __add__() , which are responsible for +,-,/,* etc operations.
"""


class MyType:
    def __init__(self,dicts:dict):
        self.dicts=dicts
        
    def __add__(self,another)->dict:
        new_dict={**self.dicts,**another.dicts} #-> add two dictionaries by + operator
        return new_dict
        
    def __gt__(self,another:dict)->bool:
        if self.dicts['age']<another.dicts['age']:
            return False
        else:
            return True

"""       
a={
    "name":"Utsav"
}
b={
    "age":22
}

m1=MyType(a)
m2=MyType(b)

m3=m1+m2
print(m3)
"""

"""
a={
    "age":23
}
b={
    "age":22
}

m1=MyType(a)
m2=MyType(b)
print(m2<m1) #---> '<' internally calls __gt__()
"""
################ METHOD OVERLOAD ########################
class X:
    def disp(self):
        print("In X")
        
class Y(X):
    
    def disp(self):
        print("overloads in Y")
        
y=Y()
y.disp()

