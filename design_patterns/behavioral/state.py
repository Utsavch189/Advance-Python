from dataclasses import dataclass
import time

STATES=['idle','select','payment']

@dataclass
class RequestedItem:
    item_no:int
    item_name:str
    quant:int
    price:int

class Items:

    items=[
        {"item_no":1,"item_name":"Coke","available":52,"price":50},
        {"item_no":2,"item_name":"Pepsi","available":22,"price":35},
        {"item_no":3,"item_name":"Chips","available":66,"price":20},
        {"item_no":4,"item_name":"Water-Bottle","available":10,"price":30},
        {"item_no":5,"item_name":"Candy","available":15,"price":10}
    ]

    @classmethod
    def display_items(cls):
        print("------------ITEMS---------------------")
        for i in cls.items:
            print(f"Item-No: {i['item_no']}  Item-Name: {i['item_name']}  Available: {i['available']}  Price: {i['price']}")
        print("------------ITEMS---------------------")
    
    @classmethod
    def one_item(cls,item_no:int)->dict:

        for i in cls.items:   
            if int(item_no)==int(i['item_no']):
                return i
        raise Exception("Wrong Item !") 
    
    @classmethod
    def modify_quantity(cls,taken:int,item_no:int)->None:
        for i in cls.items:
            if item_no==i['item_no']:
                i['available']-=taken
                break

class SelectItem:

    def select(self,quant:int,item_no:int)->RequestedItem:
        item:dict=Items.one_item(item_no=item_no)
        if quant > item.get('available'):
            raise Exception(f"Only available {item.get('available')}")
        print("Loading...")
        time.sleep(2)
        return RequestedItem(
            item_no=item.get('item_no'),
            item_name=item.get('item_name'),
            quant=quant,
            price=item.get('price')*quant
        )

class Payment:

    def pay(self,amount,req_item:RequestedItem)->RequestedItem:
        if amount != req_item.price:
            raise Exception(f"Please give {req_item.price} rs.")
        
        print("Loading...")
        time.sleep(4)

        Items.modify_quantity(taken=req_item.quant,item_no=req_item.item_no)
        print("Payment is successful!!!")
        return req_item

class StateManager:

    state:str="idle"

    def curr_state(cls)->str:
        return cls.state.lower()

    def update_state(cls,state_name:str)->None:
        if not state_name.lower() in STATES:
            raise Exception("Wrong State")
        cls.state=state_name

        return cls.action()
    
    def action(cls)->None|SelectItem|Payment:
        if cls.state=='idle':
            Items.display_items()
        elif cls.state=='select':
            return SelectItem()
        else:
            return Payment()
    
    
class VendingMachine:

    def __init__(self) -> None:
        self.state=StateManager()
    
    def client(self):
        try:
            self.state.update_state("idle")
            item_no=str(input("select item no..."))
            quant=int(input("select item quantity..."))

            select_state=self.state.update_state('select')
            item=select_state.select(quant,item_no)

            print(f"Your Item is {item.item_name} your requested quantity is {item.quant} and you have to pay {item.price} ")

            payment_state=self.state.update_state('payment')
            amount=int(input("put your amount..."))
            collected_item=payment_state.pay(amount,item)


            print("Collect Your Item....",collected_item)
            print()
            print("Now Items are...")
            self.state.update_state("idle")
        except Exception as e:
            print(e)

v=VendingMachine()
v.client()