class Pet:
    def __init__(self, name, happiness, hunger, alive):
        self.name = name
        self.happiness = happiness
        self.hunger = hunger
        self.alive = alive
    def play(self):
        self.happiness += 10
        print(f"happiness has increased to {self.happiness}")
    def feed(self):
        self.hunger += 10
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
        Name.play()
    elif hungry.lower() == "check stats":
        Name.show()
    elif hungry.lower() == "feed":
        Name.feed()
    else: 
        print("thats not an option")
                







