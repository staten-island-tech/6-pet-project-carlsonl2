'''class Pet:
    def __init__(self, name, happiness, hunger, alive):
        self.name = name
        self.happiness = happiness
        self.hunger = hunger
        self.alive = alive
    def play(self, value):
        self.happiness += value
        print(f"happiness has increased to {self.happiness}")
    def feed(self, value):
        self.hunger += value
        print(f"Your pets hunger increased to {self.hunger}")
        if self.hunger < 25:
            print("Your pet is hungry feed him soon!")
        elif self.hunger > 150:
            print("Your pet is very full, stop feeding him!")
    
        
    def show(self):
        print(f"{self.name}, happiness:{self.happiness}, hunger:{self.hunger}")
    

Name = input("What would you like to name your pet?")
Name = Pet(f"{Name}", 100, 50, True)
Name.show()
while Name.alive == True:
    hungry = input("Here are the things you can do. \n"
                "1: Play \n"
                "2: Check Stats \n"
                "3: Feed")
    if hungry.lower() == "play":
        Name.play(10)
    if hungry.lower() == "check stats":
        Name.show()
    if hungry.lower() == "feed":
        Name.feed(10)
    else:
        print("Not an option") '''


class Pet:
    def __init__(self, name, happiness, hunger, alive):
        self.name = name
        self.happiness = happiness
        self.hunger = hunger
        self.alive = alive
    def play(self, number):
        self.happiness += number
        print(f"happiness has changed to {self.happiness}")
    def feed(self, number):
        self.hunger += number
        print(f"Your pets hunger changed to {self.hunger}")
        if self.hunger == 0:
            self.alive = False
        if self.hunger < 25:
            print("Your pet is hungry feed him soon!")
        elif self.hunger > 150:
             print("Your pet is very full, stop feeding him!")
    def show(self):
        print(f"{self.name}, happiness:{self.happiness}, hunger:{self.hunger}")


Name = input("What would you like to name your pet?")
Name = Pet(f"{Name}", 100, 50, True)
Name.show()
while Name.alive == True:
    import random
    random.randint(1, 100)
    if random.randint > 50:
        Name.feed(-5)
        Name.show()
    elif random.randint < 50:
        Name.happiness(-5)
        Name.show()
    hungry = input("Here are the things you can do. \n"
                "1: Play \n"
                "2: Check Stats \n"
                "3: Feed")
    if hungry.lower() == "play":
        Name.play()
    elif hungry.lower() == "check stats":
        Name.show()
    elif hungry.lower() == "feed":
        Name.feed()         
    elif hungry.lower() != "play" or "check stats" or "feed":
        print("Thats not an option")







