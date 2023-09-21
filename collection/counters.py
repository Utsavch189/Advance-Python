from collections import Counter

"""
A counter is a sub-class of the dictionary. 
It is used to keep the count of the elements in an iterable in the form of an unordered dictionary where the 
key represents the element in the iterable and value represents the count of that element in the iterable.
https://www.digitalocean.com/community/tutorials/python-counter-python-collections-counter
"""

# With sequence of items  
print(Counter(['B','B','A','B','C','A','B',
               'B','A','C']))
    
# with dictionary 
print(Counter({'A':3, 'B':5, 'C':2}))
    
# with keyword arguments 
print(Counter(A=3, B=5, C=2))

# Example :

string="saantanu"

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
print(c.most_common(1)) # [('a', 3)] --> most time occuring
print(c.most_common()[:-2:-1]) # [('u', 1)] --> least time occuring

print()

coun = Counter()
 
coun.update([1, 2, 3, 1, 2, 1, 1, 2])
print(coun)
 
coun.update([1, 2, 4])
print(coun)

# Subtract two Counters

c1 = Counter(A=4,  B=3, C=10)
c2 = Counter(A=10, B=3, C=4)
 
c1.subtract(c2) # --> c1-c2
print(c1)

"""
We can also access all the keys and values of a counter using the keys(), values(), and items() methods. 
These methods return views of the keys, values, and key-value pairs in the counter, respectively. 
"""
print()

my_counter = Counter('abracadabra')
print(my_counter.keys())
print(my_counter.values())
print(my_counter.items())