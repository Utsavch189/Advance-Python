"""
Open/Close means Open for extension but close for modification...
If your class is bug free and in live state then dont modify it, 
just extend it...
"""
"""
In our prev example,
We create a InvoiceDao for save it in db,
"""
class Invoice:
    ...


class InvoiceDao:
    def __init__(self,invoice:Invoice) -> None:
        self.invoice:Invoice=invoice

    def save(self):
        print("save to db....")

"""
Now I want to implement save in files also
"""
# WRONG.....
class InvoiceDao:
    def __init__(self,invoice:Invoice) -> None:
        self.invoice:Invoice=invoice

    def save(self):
        print("save to db....")
    def saveFile(self):
        print("save to file....")

"""
Here Open/Close rule breaks..
So, Solution is,
"""
# Right.....
from abc import ABC,abstractmethod

class IInvoiceDao(ABC):
    @abstractmethod
    def save(self,invoice:Invoice):
        pass

class InvoiceDB(IInvoiceDao):
    def save(self, invoice: Invoice):
        print("save to db....")

class InvoiceFile(IInvoiceDao):
    def save(self, invoice: Invoice):
        print("save to file....")

"""
here we just implement our IInvoiceDao Interface....
like this we can extend rather then modify..
"""