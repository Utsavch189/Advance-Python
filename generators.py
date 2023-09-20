"""
Generators provide a space-efficient method for such data processing
as only parts of the file are handled at one given point in time.
"""

"""
suppose we have a large list of database records, and we have to find out the name[where first letter is a] from this,
"""
from faker import Faker
import time
import sys

fake=Faker()


# brute force method
begin=time.time()

def create_list():
    l=[]
    for _ in range(100):
        l.append({
            "name":fake.name(),
            "address":fake.address(),
        })
    return l

def get_res():
    my_list=create_list()
    res=[]

    for i in my_list:
        name=i.get('name')
        first_letter=(name[:1]).lower()
        if first_letter=='a':
            res.append(i)
    print("memory takes : ",sys.getsizeof(res)+sys.getsizeof(my_list))
    return res

result=get_res()

total_time=(time.time()-begin)

print("result is : ",result)
print("len : ",len(result))
print("process takes : ",total_time)

print("with generators....")

# Generators..
begin2=time.time()

def create_generator():
    for _ in range(100):
        yield {
            "name":fake.name(),
            "address":fake.address(),
        }

def get_res2():
    my_list_generator=create_generator()
    res2=[]

    for i in my_list_generator:
        name=i.get('name')
        first_letter=(name[:1]).lower()
        if first_letter=='a':
            res2.append(i)
    print("memory takes : ",sys.getsizeof(res2)+sys.getsizeof(my_list_generator))
    return res2

result2=get_res2()

total_time2=(time.time()-begin2)

print("result is : ",result2)
print("len : ",len(result2))
print("process takes : ",total_time2)

"""
According to the stats, the memory consumption is too cheap in case of generators,
to generate the same result in same time the first one takes 1104 memory space but in second way generators takes only
296 memory space.
"""