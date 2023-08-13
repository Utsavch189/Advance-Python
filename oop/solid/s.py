"""
Each and every class should have one reason to change
"""
# EX ->

class Marker:

    def __init__(self,name:str,color:str,year:int,price:int) -> None:
        self.name:str=name
        self.color:str=color
        self.year:int=year
        self.price:int=price

class Invoice:

    def __init__(self,marker:Marker,quantity:int) -> None:
        self.marker:Marker=marker
        self.quantity:int=quantity
    
    def calculate_price(self):
        return self.marker.price*self.quantity
    
    def print_invoice(self):
        print("Printing...")
    
    def save(self):
        print("save to db....")

"""
the above example is not following single responsibility...
because , calculate_price , print_invoice ,save all three ,methods should be changed..
"""
#Sol ->

class Invoice:

    def __init__(self,marker:Marker,quantity:int) -> None:
        self.marker:Marker=marker
        self.quantity:int=quantity
    
    def calculate_price(self):
        return self.marker.price*self.quantity

class InvoicePrint:
    def __init__(self,invoice:Invoice) -> None:
        self.invoice:Invoice=invoice

    def print_invoice(self):
        print("Printing...")


class InvoiceDao:
    def __init__(self,invoice:Invoice) -> None:
        self.invoice:Invoice=invoice

    def save(self):
        print("save to db....")
