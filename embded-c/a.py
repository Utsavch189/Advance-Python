from ctypes import *
import time

so_file='./a.so'
# $ cc -fPIC -shared -o my_functions.so my_functions.c [to convert .so file]

c_func=CDLL(so_file)

start1=time.time()
s1=c_func.square(5)
print("s1 : ",s1)
print(c_func.getMemoryUsage())
print("total time : ",time.time()-start1)

#print()
#
#start2=time.time()
#s2=5**2
#print("s2 : ",s2)
#print("total time : ",time.time()-start2)
