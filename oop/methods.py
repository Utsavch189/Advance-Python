class Calc:

    window:bool=False

    def __init__(self, a:int,b:int):
        self.a=a
        self.b=b
    
    @classmethod #---------> class methods for class vars
    def getWindow(cls)->bool:
        return cls.window
    
    @classmethod
    def setWindow(cls,stat:bool):
        cls.window=stat
    
    def add(self): #------------> self is instance method
        print("sum : ",self.a+self.b)
    
    @staticmethod #--------------> static methods for static things
    def message(your_msg:str):
        print(your_msg)
    
c1=Calc(8,17)
c2=Calc(10,4)

if Calc.getWindow():
    Calc.message("window is already True....")
    c1.add()
    c2.add()
    Calc.message("done.....")
else:
    Calc.message("please wait for window becoming True....")
    Calc.setWindow(stat=True)
    c1.add()
    c2.add()
    Calc.message("done.....")
