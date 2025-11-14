

class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory
        
        
    def buy(self, item):
        self.inventory.append(item)
   

Jordan = Hero("Jordan", 100, ["Wooden Sword"])

Shop = [ 
{ "name" : "Iron Sword", "attack" : 35},
{ "name" : "Ice Sword", "attack" : 50},
{ "name" : "Fire Sword", "attack" : 60}
]

Jordan.buy(Shop[2])

Jordan.buy(Shop[0])
        
print(Jordan.__dict__)      
        


