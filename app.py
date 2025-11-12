class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory
        
            
            
    
    def buy(self, item):
        self.inventory.append(item)
        

Jordan = Hero("Jordan", 100, ["Wooden Sword"])
alive = True
while alive == True:
    


