def password(Email, Password):
    mail_valid = False
    pass_valid = False
    if "@" not in Email:
        print("not a valid email")
    if not isinstance(Email, str) or not isinstance(Password, str):
        print("Email must be a string")
        mail_valid = True
    if mail_valid == True:
        for i in Password:
            Characters = 0
            Special_Characters = ["!", "@"]
            Characters += 1
        if Characters < 8:
            print("Your password must be atleast 8 characters long")
        if not any(Password.isdigit() for i in Password):
            print("Password must have 1 number")
        if not any(Password.isupper() for i in Password):
            print("Password must have atlest 1 uppercase letter")
        if not any(a in Password for a in Special_Characters):
            print("Password must contain atlest 1 special character")
            pass_valid = True

password("DFSDFSD@", ["dsadasd"])         

            
           





