"""
Defaultdict is a container like dictionaries present in the module collections. 
Defaultdict is a sub-class of the dictionary class that returns a dictionary-like object. 
The functionality of both dictionaries and defaultdict are almost same except for the fact that defaultdict never raises a KeyError. 
It provides a default value for the key that does not exists
"""
from collections import defaultdict

a=dict()

a['a']=1
a['b']=2

#print(a['c']) # --> KeyError: 'c'


b=defaultdict(int)

b['a']=1
b['b']=2
print(b)
print(b['c']) # return 0

c=defaultdict(lambda : "not found!")

c['a']=1
c['b']=2
print(c)
print(c['c']) # return "not found!"

for k,v in c.items():
          print(k," : ",v)  

"""
a  :  1
b  :  2
c  :  not found!
"""
