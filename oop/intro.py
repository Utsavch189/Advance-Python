

class Person1:

    def setName(self,name:str):
        self.name=name

    def getName(self)->str:
        return self.name
    
class Person2:
    msg="hi"

    def __init__(self, name:str):
        self.name=name

    def getName(self)->str:
        print(self.msg)
        return self.name

if __name__=="__main__":
    #p=Person1()
    #p.setName("Utsav")
    #print(p.getName())
    #p1=Person2("utsav")
    #print(p1.getName())

    #another type of declaring......
    p1=Person2("utsav")
    p2=Person2("supu")
    print(Person2.getName(p1)) #----> self is pointing to p1 now
    print(Person2.getName(p2)) #----> self is pointing to p2 now