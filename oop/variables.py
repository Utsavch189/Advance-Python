class A:

    name="utsav" #-------> class var

    def __init__(self, age):
        self.age=age #---------> instance var

a=A(5)
b=A(55)
print("in a instace,before update : ",a.age)
print("in a instace,before update : ",A.name or a.name)

print("in b instace,before update : ",b.name or A.name)
print("in b instace,before update : ",b.age)

a.age=8 #--------> instace vars are particular for instances
b.age=40 #--------> instace vars are particular for instances
A.name="sashi" #------> class var is global for any instance of this class
print("in a instace,after update : ",a.age)
print("in a instace,after update : ",A.name or a.name)

print("in b instace,after update : ",b.name or A.name)
print("in b instace,after update : ",b.age)