
"""
builder pattern is a advance form of factory pattern. In those situations where we need to pass too many parameters in constructor , even 
we don't need all parameters to create that object.
"""

class Burger:

    sauces:str="No"
    letuces:str="No"
    cheeses:str="No"
    number_of_pattys:int=0

    def __init__(self,inst) -> None:
        self.sauces=inst.sauce
        self.letuces=inst.letuce
        self.cheeses=inst.cheese
        self.number_of_pattys=inst.number_of_patty

    def __str__(self) -> str:
        return f"I am a burger with sauce: {self.sauces}, letuce: {self.letuces}, cheese: {self.cheeses}, number_of_patty: {self.number_of_pattys}"
    
    class BurgerBuilder:

        sauce:str="No"
        letuce:str="No"
        cheese:str="No"
        number_of_patty:int=0
        
        def setSauce(self,sauce:str):
            self.sauce=sauce
            return self
        
        def setLetuce(self,letuce:str):
            self.letuce=letuce
            return self
        
        def setCheese(self,cheese:str):
            self.cheese=cheese
            return self
        
        def setNumberOfPatty(self,number_of_patty:int):
            self.number_of_patty=number_of_patty
            return self
        
        def build(self):
            ob=Burger(self)
            return ob

if __name__=="__main__":
    burger1=Burger.BurgerBuilder().setSauce("Tommato").setCheese("Extra").setNumberOfPatty(5).build()
    print(burger1)
    burger2=Burger.BurgerBuilder().setSauce("Onnion").setCheese("Less").setNumberOfPatty(3).setLetuce("yes").build()
    print(burger2)
