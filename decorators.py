"""
a decorator that takes the passed string into original func, and returns uppercase of it..
"""
def dec(func):
    def inner(*args, **kwargs):
        print("1. into decorator")
        for v in args:
            val=v.upper()
        return func(val)
    return inner

@dec
def test(st:str)->str:
    print("into func")
    return st

print(test("hi i am utsav chatterjee"))
print()

"""
a decorator that takes the passed string into original func, and returns uppercase of it and also takes param into decorator itself..
"""
def dec(value):
    def wrapper(func):
        def inner(*args, **kwargs):
            print("2. into decorator")
            print("passed value in decorator : ",value)
            for v in args:
                val=v.upper()
            return func(val)
        return inner
    return wrapper

@dec(value="ok")
def test(st:str)->str:
    print("into func")
    return st

print(test("hello world"))