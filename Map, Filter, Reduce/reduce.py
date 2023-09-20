from functools import reduce  

"""
Python, reduce() is a built-in function that applies a given function to the elements of an iterable, 
reducing them to a single value.
"""
data = [1, 2, 3, 4, 5] 

sum_all_elem=lambda a,b:a+b

res1=reduce(sum_all_elem,data)

print(res1)