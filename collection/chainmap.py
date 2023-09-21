"""
Python contains a container called “ChainMap” which encapsulates many dictionaries into one unit. 
"""

from collections import ChainMap  
       
       
d1 = {'a': 1, 'b': 2} 
d2 = {'c': 3, 'd': 4} 
d3 = {'e': 5, 'f': 6} 
    
# Defining the chainmap  
c = ChainMap(d1, d2, d3)  
       
print(c)

print(c.maps)
print(c.keys())
print(c.values())

for k,v in c.items():
          print(k," : ",v)


print(list(c.keys()))
print(list(c.values()))

d4={'g':3,'h':1,'d':9}
c1=c.new_child(d4) # --> add new dict to first pos

print(c1.maps)

print("before reversed : ",c1['d']) # return 9 because first ocuuring d's value is 9.

c1.maps=reversed(c1.maps)

print("after reversed : ",c1['d']) # return 4 because first ocuuring d's value is 4 after reversing.