for i in range(3, 0, -1):
        print("==Login==")
        user = input("username : ")
        password = input("Password : ")

        if user == "admin" and password == "admin": 
            print("Login Success!!")
            break
        else:
            print("Incorrect Username or Password")
            if i > 1:
                print(f"{i-1} more chance left\n")
            else:
                print("You are no longer able to login\n")