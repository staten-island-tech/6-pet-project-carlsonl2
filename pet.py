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
        print(f"{self.name}, happiness:{self.happiness}, hunger:{self.hunger}")

Name = input("What would you like to name your pet?")
Name = Pet(f"{Name}", 100, 50)
Living = True

if Name.hunger < 25:
    print("Your pet is hungry feed him soon!")
elif Name.hunger > 150:
    print("Your pet is very full, stop feeding him!")
elif Name.hunger > 200:
    Living = False
    print("Your pet died from overfeeding")
elif Name.hunger == 0 or Name.hunger < 0:
    Living = False
    print("your pet died of hunger.")



import random
while Living == True:
    randon_ = random.randint(1, 50)
    if randon_ > 25:
        Name.hunger -= 5
    Options = input("What would you like to do? 1.Play  2.Feed")
    if Options.lower() == "play":
        Name.play(10)
        Name.show()
    elif Options.lower() == "feed":
        Name.feed(10)
        Name.show()
                                              