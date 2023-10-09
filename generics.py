"""
suppose I have a func that receives a list and print it.
"""

def func(elm):
    try:
        for i in elm:
            print(i,end=" ")
        print()
    except Exception as e:
        print(e)

a=['a',2,True,{"name":"utsav"}]
func(a)

"""
We want now that func adds a list values and print it.
Now, the problem is anybody should put any mixed list here or any other data type here, 
because no data type is declared for elm.
Now , we need to modify our func that should only accepts list.
"""

from typing import List,TypeVar,Dict,Generic

def func1(elm:List[int])->None:
    try:
        val=0
        for i in elm:
            val=val+i
        print(val)
    except Exception as e:
        print(e)

a=[1,2,3]
func1(a) # --> will tell what it expects

"""
It's called type hinting for a reason: you're giving a hint 
about what a variable should be to the IDE or to anyone else reading your code. 
At runtime, 
the type hints don't actually mean anything - they exist for documentation and usability by other developers. 
"""

"""
However, even with this example, let alone a larger real world example working with user defined types, 
these type hints don’t capture something that we know to be true. 
We know that our method will be used with lists of a single type. 
We also know that the return type will match the type of the items in the list, 
so let’s capture these things in the code.
"""

T=TypeVar("T")

def func2(elm:List[T])->None:
    try:
        for i in elm:
            print(i,end=" ")
        print() 
    except Exception as e:
        print(e)

a=[(1,2),(9,2)]
func2(a)

K = TypeVar("K")
V = TypeVar("V")

def get_item(key: K, container: Dict[K, V]) -> V:
    return container[key]

test: Dict[str, int] = {"k": 1}
print(get_item("k", test))

"""
NOTE : 
T = TypeVar("T", str, int) # T can only represent types of int and str
T = TypeVar("T", bound=int) # T can only be an int or subtype of int
"""

# Generic Classes

"""
Generics are not just used for function and method parameters. 
They can also be used to define classes that can contain, or work with, 
multiple types. These “generic types” allow us to state what type, or types, 
we want to work with for each instance when we instantiate the class.
"""

T = TypeVar("T",int,str)

class Registry(Generic[T]):
    def __init__(self) -> None:
        self._record:Dict[str,T]={}
    
    def sets(self,name:str,rec:T)->None:
        self._record[name]=rec
    
    def gets(self,name:str)->T:
        return self._record[name]

family_name_reg = Registry[str]()
family_age_reg = Registry[int]()

family_name_reg.sets("husband", "steve")
family_name_reg.sets("dad", "john")
    
family_age_reg.sets("steve", 30)
family_age_reg.sets("john",66)

name_of_husband=family_name_reg.gets("husband")
age_of_husband=family_age_reg.gets(name_of_husband)

print(f"{name_of_husband} : {age_of_husband}")