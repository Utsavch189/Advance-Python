from collections import Counter

"""
A counter is a sub-class of the dictionary. 
It is used to keep the count of the elements in an iterable in the form of an unordered dictionary where the 
key represents the element in the iterable and value represents the count of that element in the iterable.
"""

# With sequence of items  
print(Counter(['B','B','A','B','C','A','B',
               'B','A','C']))
    
# with dictionary 
print(Counter({'A':3, 'B':5, 'C':2}))
    
# with keyword arguments 
print(Counter(A=3, B=5, C=2))

# Example :

string="santanu"

c=Counter(string)
print(c)
# Counter({'a': 2, 'n': 2, 's': 1, 't': 1, 'u': 1})
for i in c.keys():
    print(i ," : ",c.get(i))

"""
s  :  1
a  :  2
n  :  2
t  :  1
u  :  1
"""