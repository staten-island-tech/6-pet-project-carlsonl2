def password(Email, Password):
    Characters = 0

    if "@" not in Email:
        print("Email must contain an @ symbol, try again")
    elif "@" in Email:
        print("Create a PassWord")
        for i in Password:
            Characters += 1
        if Characters < 8:
            print("Your password must be atleast 8 characters long")
        if str.isdigit(Email):
            

            
           
password("carlson@", "P32ikeo")

