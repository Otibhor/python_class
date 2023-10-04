def reg():
    name = input("Enter Name: ")
    process = True
    while process:
        password = input("Enter Password: ")
        if len(password) > 8:
            print("password must not be more than 8 characters")
            print('Please try again!')
        else:
            print("Registration Successful!")
            process = False
            return name, password

reg()