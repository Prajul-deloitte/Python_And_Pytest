from login import loginuser
from RegisterUser import registerUser

x = 5
print("******Welcome to BookMyShow******* ")
while x != 3:
    print("1.Login\n2.Register new account\n3.Exit")
    x = int(input("Enter : "))
    if x == 1:
        loginUser = loginuser()
        loginUser.enter()
        loginUser.checkUser()
    if x == 2:
        register = registerUser()
        register.registration()
    if x == 3:
        exit()