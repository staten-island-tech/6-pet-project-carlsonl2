def password(Email):
    accepted = False
    while accepted == False:
        if "@" not in Email:
            print("Email must contain an @ symbol, try again")
password("carlsonl2")

