"""
It provides a way to create simple, lightweight data structures similar to a class, 
but without the overhead of defining a full class. Like dictionaries, 
they contain keys that are hashed to a particular value. On the contrary, 
it supports both access from key-value and iteration, the functionality that dictionaries lack.
"""

from collections import namedtuple

Student=namedtuple('Student',['name','roll','age'])

r1=Student('supu','10','21')
r2=Student('utsav','05','22')

print(r1,r2)

print(r1.name," ",r2.name)

print(r1._asdict()) # data form of dict
print(r1.__getnewargs__()) # data form of tuple


li=['sourav','27','21']

r3=Student._make(li)

print(r3)

dct={"name":"sanu","roll":"28","age":"27"}

r4=Student(**dct)

print(r4)

print(r4._fields)

r4_replaced=r4._replace(name='sanu jana')

print(r4_replaced)
