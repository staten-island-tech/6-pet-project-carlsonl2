class Pet:
    def __init__(self, name, happiness, hunger, alive):
        self.name = name
        self.happiness = happiness
        self.hunger = hunger
        if self.hunger < 25:
            print("Your pet is hungry feed him soon!")
        elif self.hunger > 150:
             print("Your pet is very full, stop feeding him!")
        
            
    def play(self, value):
        self.happiness += value
        print(f"happiness has increased to {self.happiness}")
    def feed(self, value):
        self.hunger += value
        print(f"Your pets hunger increased to {self.hunger}")
    def show(self):
        print(f"{self.name}, happiness:{self.happiness}, hunger:{self.hunger}")
    def life(self):
        self.alive = True
        if self.alive != True:
            print("Your pet is dead")

Name = input("What would you like to name your pet?")
Name = Pet(f"{Name}", 100, 50)








