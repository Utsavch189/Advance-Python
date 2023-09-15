"""
Something which can be iterated is called iterables.Like, list,set,tuple,dict,str etc.
iterable objects has a magic method named __iter__() .

During iteration , the state which points to that iterable, is called iterator.
An iterator object is an object that implements the __next__() dunder method that returns the next element of the iterable object
and raises a StopIteration error if the iteration is done
"""

"""
Create a custom range function which is a iterable and also a iterator
"""

class CustomRange:

    def __init__(self,start:int,end:int) -> None:
        self.start=start
        self.end=end
    
    def __iter__(self): # --> as a iterable it returns it's own object
        return self
    
    def __next__(self): # --> as a iterator
        if self.start>=self.end:
            raise StopIteration
        curr=self.start
        self.start+=1
        return curr

num=CustomRange(0,9)
# access as a iterable by 'for' iterator

#for i in num:
#    print(i,end=" ")

# access directly as a iterator by directly overloading __next__()

#print(next(num))
#print(next(num))
#print(next(num))
#print(next(num))

class Sentence:

    def __init__(self,s:str) -> None:
        self.s=s.split(" ")
        self.l=len(self.s)-1
        self.c=0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.c>self.l:
            raise StopIteration
        curr=self.s[self.c]
        self.c+=1
        return curr

sentence1=Sentence("my name is utsav chatterjee!")
sentence2=Sentence("hello world")

for i in sentence1:
    print(i)

print()

for i in sentence2:
    print(i)