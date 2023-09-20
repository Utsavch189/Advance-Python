data = [1, 2, 3, 4, 5] 

"""
Python's map() method applies a specified function to each item of an iterable
(such as a list, tuple, or string) and then returns a new iterable containing the results.
"""

create_pow=lambda x:x**x
add=lambda x:x+x
multiply=lambda x:x*x

res1=map(create_pow,data)
res2=map(add,data)
res3=map(multiply,data)

for i in res1:
    print(i,end=" ")

print()

for i in res2:
    print(i,end=" ")

print()


for i in res3:
    print(i,end=" ")