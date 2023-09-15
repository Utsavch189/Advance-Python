"""
Comprehensions in Python provide us with a short and concise way to construct new sequences (such as lists, sets, dictionaries, etc.) using previously defined sequences. Python supports the following 4 types of comprehension:

List Comprehensions
Dictionary Comprehensions
Set Comprehensions
Generator Comprehensions
"""

# List :

lists=[1,2,3,4,5,6,7,9,8,10]
res=[]

# 1. append numbers from lists to res

# general looping approach :

for i in lists:
    res.append(i)
print(res)

# with comprehension

res=[i for i in lists]
print(res)

# 2. even numbers append into res
res=[]
# general looping approach :

for i in lists:
    if i%2==0:
        res.append(i)
print(res)

# with comprehension

res=[i for i in lists if i%2==0]
print(res)

# 3. numbers*numbers append into res
res=[]
# general looping approach :

for i in lists:
    res.append(i*i)
print(res)

# with comprehension

res=[i*i for i in lists]
print(res)

# 4. tuple of (numbers,'odd/even') append into res
res=[]
# general looping approach :

for i in lists:
    if i%2==0:
        res.append((i,'even'))
    else:
        res.append((i,'odd'))
print(res)

# with comprehension

res=[(i,'even') if i%2==0 else (i,'odd')for i in lists]
print(res)

# Dict :

res_dict={}

# 1. dict of numbers:'odd/even' append into res_dict
# general looping approach :

for i in lists:
    if i%2==0:
        res_dict[i]='even'
    else:
        res_dict[i]='odd'
print(res_dict)

# with comprehension

res_dict={(i if i%2==0 else i):('even' if i%2==0 else 'odd')for i in lists}
print(res_dict)

# 2. dict of numbers:index append into res_dict
res_dict={}
# general looping approach :

for i,v in enumerate(lists):
    res_dict[v]=i
print(res_dict)

# with comprehension

res_dict={v:i for i,v in enumerate(lists)}
print(res_dict)

# 3. dict of numbers:index append into res_dict if numbers are odd
res_dict={}
# general looping approach :

for i,v in enumerate(lists):
    if v%2!=0:
        res_dict[v]=i
print(res_dict)

# with comprehension

res_dict={v:i for i,v in enumerate(lists) if v%2!=0}
print(res_dict)

# Set :
lists=[1,2,3,2,3,9,4,5,6,7,9,8,10]
res_set=set()

# 1. add numbers from lists to res_set
# general looping approach :

for i in lists:
    res_set.add(i)
print(res_set)

# with comprehension

res_set={i for i in lists}
print(res_set)

# Generators :

def gen_func(l):
    for i in l:
        yield i*i

my_gen=gen_func(lists)

for i in my_gen:
    print(i,end=" ")
print()
# with comprehension
my_gen2=(i*i for i in lists)

for i in my_gen2:
    print(i,end=" ")