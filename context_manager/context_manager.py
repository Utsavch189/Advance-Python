"""
Managing Resources: In any programming language, the usage of resources like 
file operations or database connections is very common. But these resources are 
limited in supply. Therefore, the main problem lies in making sure to release 
these resources after usage. If they are not released then it will lead to resource 
leakage and may cause the system to either slow down or crash. It would be very helpful 
if users have a mechanism for the automatic setup and teardown of resources. In Python, 
it can be achieved by
the usage of context managers which facilitate the proper handling of resources
"""

# In Pyhton 'with' keyword uses to perform it.

with open('test.txt','r') as f:
    print(f.read())

# in 'with' statement the '__enter__' dunder method is called! After end of that block '__exit__' method is called.

class Main:

    def __init__(self,msg) -> None:
        self.__msg=msg

    def read(self):
        #raise Exception("sorry")
        print(self.__msg)

class Myclass:

    def __init__(self,msg) -> None:
        self.__msg=msg

    def __enter__(self):
        """
        This method handles the setup logic and is called when entering 
        a new with context. Its return value is bound to the with target variable.
        """
        print('enter')

        self=Main(self.__msg)
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        """
        This method handles the teardown 
        logic and is called when the flow 
        of execution leaves the with context. 
        If an exception occurs, then exc_type, exc_value, and exc_tb hold the exception type, 
        value, and traceback information, respectively.
        """
        print(exc_value)

        return True 
        """
        Note that you need to return True from __exit__ if you want to suppress the thrown error 
        if there is any
        """

    


with Myclass('oi') as m:
    m.read()