"""
proxy is a shadow of original object, with some more restrictions,
"""
from abc import ABC,abstractmethod
import time
from collections import OrderedDict

STUDENTS:list[dict]=[
    {"id":1,"name":"utsav"},
    {"id":2,"name":"supu"},
    {"id":3,"name":"soubhagya"},
    {"id":4,"name":"sourav"},
    {"id":5,"name":"arijit"}
]

class I_DB(ABC):

    @abstractmethod
    def create(self,data:dict)->None:pass

    @abstractmethod
    def get(self,id:int)->dict:pass

    @abstractmethod
    def put(self,id:int,name:str)->None:pass

    @abstractmethod
    def delete(self,id:int)->None:pass

class DB(I_DB):

    def __init__(self) -> None:
        self.db="Students"
        self.students:list[dict]=STUDENTS
    
    def __str__(self) -> str:
        return self.db
    
    def create(self,data:dict)->None:
        self.students.append(data)

    def get(self, id: int) -> dict:
        time.sleep(2)
        for i in self.students:
            if i['id']==id:
                return i
        

    def put(self, id: int, name: str) -> None:
        for i in self.students:
            if i['id']==id:
                i['name']=name
                return
        
    
    def delete(self, id: int) -> None:
        for i in self.students:
            if i['id']==id:
                self.students.remove(i)
                return
        

class Cache:

	def __init__(self, capacity=32):
		self.cache = OrderedDict()
		self.capacity = capacity

	def get(self, key):
		if key not in self.cache:
			return False
		else:
			self.cache.move_to_end(key) # --> while data is found , it re-positioned to last thats why it's not be recognized through LRU. 
			return self.cache[key]

	def put(self, key, value):
		self.cache[key] = value
		self.cache.move_to_end(key)
		if len(self.cache) > self.capacity:
			self.cache.popitem(last = False) # --> remove first added item as LRU concept.
			
	def delete(self,key):
		self.cache.pop(key)

"""
Proxy class is the mediator between db and cache
"""
class Proxy(I_DB):
     
    def __init__(self) -> None:
        self.db=DB()
        self.cache=Cache()
        
    def create(self, data: dict) -> None:
        self.db.create(data=data)
    
    def get(self, id: int) -> dict:
        if self.cache.get(key=id):
            print('from cache')
            return self.cache.get(key=id)
        else:
            print('from db')
            data=self.db.get(id=id)
            self.cache.put(key=id,value=data)
            return data
    
    def put(self, id: int, name: str) -> None:
         self.db.put(id,name)
         if self.cache.get(key=id):
            self.cache.put(key=id,value={"id":id,"name":name})

    def delete(self, ids: int) -> None:
        self.db.delete(ids)
        if self.cache.get(key=ids):
            self.cache.delete(ids)
    

if __name__=='__main__':
     db=Proxy()
     while True:

        print("1. Create \n 2. Get \n 3. Put \n 4. Delete")
        opt=int(input('Enter options... : '))
        if opt==1:
             ids=int(input('Enter id... : '))
             names=str(input('Enter name... : '))
             data={"id":ids,"name":names}
             db.create(data)
        elif opt==2:
             idss=int(input('Enter id... : '))
             print(db.get(idss))
        elif opt==3:
             idsss=int(input('Enter id... : '))
             name=str(input('Enter name... : '))
             db.put(idsss,name)
        elif opt==4:
             idd=int(input('Enter id... : '))
             db.delete(idd)
        else:
             break