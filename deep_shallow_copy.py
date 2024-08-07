import copy

"""
In Python, we use = operator to create a copy of an object. 
You may think that this creates a new object; it doesn't. 
It only creates a new variable that shares the reference of the original object.
"""

print("assignment operator------")
l1=[1,2,[6,7]]
l2=l1
print(id(l1) ," ",id(l2)) 
# 138537929182016   138537929182016
l2[2][0]=10
print(l1," ",l2)
# [1, 2, [10, 7]]   [1, 2, [10, 7]] --> '=' operator actually creates a reference of that actual object thats why both are changed, no matter it's nested or not

l2[0]=3
print(l1," ",l2)
# [3, 2, [10, 7]]   [3, 2, [10, 7]]

# Shallow Copy
"""
A shallow copy creates a new object which stores the reference of the original elements.

So, a shallow copy doesn't create a copy of nested objects, 
instead it just copies the reference of nested objects. 
This means, a copy process does not recurse or create copies 
of nested objects itself.
"""
print("shallow------")
l1=[1,2,[6,7]]
l2=copy.copy(l1)
print(id(l1) ," ",id(l2)) 
# 140021985328064   140021985324736
l2[2][0]=10
print(l1," ",l2)
# [1, 2, [10, 7]]   [1, 2, [10, 7]] --> shallow copy doesn't actually clone the nested ones
# but,
l2[0]=3
print(l1," ",l2)
# [1, 2, [10, 7]]   [3, 2, [10, 7]] --> only l2 changed because that '0' indexed element was not nested ones

# Deep Copy
"""
What is Deep copy in Python?
A deep copy creates a new compound object before inserting copies of the items 
found in the original into it in a recursive manner. It means first 
constructing a new collection object and then recursively populating 
it with copies of the child objects found in the original. 
In the case of deep copy, a copy of the object is copied into another object. 
It means that any changes made to a copy of the object do not reflect in 
the original object. 
"""

print("deep------")
l1=[1,2,[6,7]]
l2=copy.deepcopy(l1)
print(id(l1) ," ",id(l2)) 
# 140021985328064   140021985324736
l2[2][0]=10
print(l1," ",l2)
# [1, 2, [6, 7]]   [1, 2, [10, 7]] --> deep copy actually clones the nested ones thats why only l2 nested element is changed

l2[0]=3
print(l1," ",l2)
# [1, 2, [10, 7]]   [3, 2, [10, 7]]