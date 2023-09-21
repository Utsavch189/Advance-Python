from ctypes import *
import glob

libfile = glob.glob('build/*/b*.so')[0]
lib='./b.so'
c_funcs=CDLL(lib)

print(c_funcs.add(1,2))