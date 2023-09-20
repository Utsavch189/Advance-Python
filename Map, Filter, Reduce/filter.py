data = [1, 2, 3, 4, 5] 

"""
The filter() function in Python filters elements from an iterable based on a 
given condition or function and returns a new iterable with the filtered elements.
"""

find_odd=lambda x:x%2==1
find_even=lambda x:x%2==0

res1=filter(find_odd,data)
res2=filter(find_even,data)

for i in res1:
    print(i,end=" ")

print()

for i in res2:
    print(i,end=" ")