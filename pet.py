class Pet:
    def __init__(self, name, happiness, hunger):
        self.name = name
        self.happiness = happiness
        self.hunger = hunger
    def play(self, value):
        self.happiness += value
        print(f"happiness has increased to {self.happiness}")
    def feed(self, value):
        self.hunger += value
    def show(self):
        print(f"{self.name}, happiness:{self.happiness}")

Name = input("What would you like to name your pet?")
Name = Pet(f"{Name}", 100)

food_list = ["Dogfood", "Meat"]

Living = True
while Living == True:
    Options = input("What would you like to do? 1.Play  2.Feed")
    if Options.lower() == "play":
        Name.play(10)
        Name.show()
    if Options.lower() == "feed":   
        Food = input(f"What would You like to feed him? {food_list}")                                                                                                                          