
class Outer:
    
    def __init__(self,name:str,age:int,address:str):
        self.name=name
        self.age=age
        self.inner=self.Inner(address)
        
    def getNameAge(self):
        print("name and age of outer : ",self.name,self.age)
        
    class Inner:
        
        def __init__(self,address:str):
            self.address=address
        
        def getAddress(self):
            print("address is in inner : ",self.address)
            

#o=Outer("Utsav",22,"Guptipara")
#o.getNameAge()
#i=o.inner
#i.getAddress()


#o1=Outer("Supu",21,"Danlop")
#o1.getNameAge()
#i1=o1.inner
#i1.getAddress()

################# MULTIPLE INNER CLASS ####################3

class Outer:
    
    def __init__(self,name:str,age:int,address:str,pin:int):
        self.name=name
        self.age=age
        self.inner1=self.Inner1(address)
        self.inner2=self.Inner2(pin)
        
    def getNameAge(self):
        print("name and age of outer : ",self.name,self.age)
        
    class Inner1:
        
        def __init__(self,address:str):
            self.address=address
        
        def getAddress(self):
            print("address is in inner1 : ",self.address)
    
    class Inner2:
    
        def __init__(self,pin:int):
            self.pin=pin
            
        def getPinCode(self):
            print("pin code is in inner2 : ",self.pin)
            
            
#o=Outer("Utsav",22,"Guptipara",712512)
#o.getNameAge()
#i1=o.inner1
#i1.getAddress()
#i2=o.inner2
#i2.getPinCode()

######################### MULTILEVEL INNER CLASS ####################

class Outer:
    
    def __init__(self,a:int,b:int):
        self.a=a
        self.b=b
        self.inner=self.Inner(a,b)
        
    def getAandB(self):
        print("a and b of outer : ",self.a,self.b)
        
    class Inner:
        
        def __init__(self,a:int,b:int):
            self.a=a
            self.b=b
            self.subinner=self.SubInner(a,b)
        
        def getMultiply(self)->float:
            print("multiply is in inner : ",self.a*self.b)
            
        class SubInner:
            
            def __init__(self,a:int,b:int):
                self.a=a
                self.b=b
            
            def getDivison(self)->float:
                print("multiply is in subinner : ",self.a/self.b)
                

o=Outer(5,6)
o.getAandB()

i=o.inner
i.getMultiply()

si=i.subinner
si.getDivison()