class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory
        work = input("Work Options : Coding")
        if work == "Coding":
            self.money += 15
    
    def buy(self, item):
        self.inventory.append(item)
        

Jordan = Hero("Jordan", 100, ["Wooden Sword"])

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # double underscore means "private"
       
    
    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(f"{self.owner} has ${self.__balance}")

