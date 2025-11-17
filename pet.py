class Pet:
    def __init__(self, name, happiness):
        self.name = name
        self.happiness = happiness
    def play(self, value):
        self.happiness += value
    def show(self):
        print(f"{self.name}, {self.happiness}")

Name = input("What would you like to name your pet?")
Name = Pet(f"{Name}", 100)

Living = True
while Living == True:
    Options = input("What would you like to do? 1.Play")
    if Options.lower() == "play":
        Name.play(10)
        print(Name.show())
                                                                                                                                                       