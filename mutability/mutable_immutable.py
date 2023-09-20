"""
Mutable objects are those that allow you to change their value or data in place without affecting the object's identity. 
In contrast, immutable objects don't allow this kind of operation.
"""

# Mutable,[set,list,dict]

my_list=[1,2,3]

lists=my_list

print("lists : ",lists)
print("my_list : ",my_list)

"""
lists :  [1, 2, 3]
my_list :  [1, 2, 3]
"""

print("after append 4 to my_list")
my_list.append(4)

print("lists : ",lists)
print("my_list : ",my_list)

"""
lists :  [1, 2, 3, 4]
my_list :  [1, 2, 3, 4]
"""

print("after append 5 to lists")
lists.append(5)

print("lists : ",lists)
print("my_list : ",my_list)

"""
lists :  [1, 2, 3, 4, 5]
my_list :  [1, 2, 3, 4, 5]
"""

print("memory address id of my_list : ",id(my_list))
print("memory address id of lists : ",id(lists))
print("are lists and my_list same? ",my_list is lists)
print("thats why they are mutable")

# Immutable,[int,float,str,tuple]
print()
a=10
b=a

print("a : ",a)
print("b : ",b)

print("after a=5")
a=5

print("a : ",a)
print("b : ",b)

print("memory address id of a : ",id(a))
print("memory address id of b : ",id(b))
print("are a and b same? ",a is b)
print("thats why they are immutable")
