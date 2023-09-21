"""
An OrderedDict is a dictionary subclass that remembers the order that keys were first inserted. The only difference between dict() and OrderedDict() is that:

OrderedDict preserves the order in which the keys are inserted. A regular dict doesn’t track the insertion order and iterating it gives the values in an arbitrary order.
By contrast, the order the items are inserted is remembered by OrderedDict.
"""
from collections import OrderedDict

# 1. Key value Change: If the value of a certain key is changed, the position of the key remains unchanged in OrderedDict.

print("Before:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
for key, value in od.items():
    print(key, value)
 
print("\nAfter:\n")
od['c'] = 5
for key, value in od.items():
    print(key, value)


# 2. Deletion and Re-Inserting: Deleting and re-inserting the same key will push it to the back as OrderedDict, however, maintains the order of insertion.

print("Before deleting:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
 
for key, value in od.items():
    print(key, value)
 
print("\nAfter deleting:\n")
od.pop('c')
for key, value in od.items():
    print(key, value)
 
print("\nAfter re-inserting:\n")
od['c'] = 3
for key, value in od.items():
    print(key, value)

"""
OrderedDict is part of the collections module in Python.
It provides all the methods and functionality of a regular dictionary, 
as well as some additional methods that take advantage of the ordering of the items. 
Here are some examples of using OrderedDict in Python:
"""
print()

# Create an ordered dictionary of key-value pairs
my_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
 
# Add a new item to the end of the dictionary
my_dict['d'] = 4
 
# Add a new item at a specific position in the dictionary
# my_dict.update({'e': 5, 'f': 6}) or below
my_dict.update([('e', 5), ('f', 6)])
my_dict.move_to_end('e', last=False)
my_dict.move_to_end('a')
 
# Iterate over the dictionary in the order in which items were added
for key, value in my_dict.items():
    print(key, value)


"""
Time Complexity:

Get item(Key): O(1)
Set item(key, value): O(1)
Delete item(key): O(n)
Iteration: O(n)
"""