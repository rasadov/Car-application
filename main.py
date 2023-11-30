from database import login, register, dashboard, add, username_exist, show_cars, show_car

enter = ""
user = 0

while (enter != "exit"):
    if user == 0:
        enter = input("log in or register? ")
        if enter == "log in":
            user = input("Enter username ")
            password = input("Enter password ")
            ans = login(user, password)
            if (ans == 0):
                print("No account like this was found")
                continue
        if enter == "register":
            user = input("Create a username: ")
            if username_exist(user) == False:
                passwordofuser = input("Create a password: ")
                while len(passwordofuser) < 8:
                    passwordofuser = input(
                        "It should be 8 characters minimum: ")
                nameofuser = input("Enter name ")
                surnameofuser = input("Enter surname ")
                bdofuser = input("Enter birthday ")
                register(user, nameofuser, surnameofuser,
                         bdofuser, passwordofuser)
                print("New account registrated")
                user = 0
                continue
            else:
                print("This username is already taken")
                user = 0
                continue
    if username_exist(user) != True:
        print("First you have to log in")
        user = 0
        continue
    if user != "":
        enter = input("""-Buy a car
-Sell a car
-My account
-Log out
""")
    if enter == "buy a car":
        show_cars()
        enter = input("which car you wanna buy? ")
        show_car(enter)
    if enter == "sell a car":
        producer = input("Enter the producer of the car: ")
        model = input("Enter the model of the car: ")
        type = input("Enter the type of the car (sedan, suv, sportcar,...): ")
        year = input("Enter the year of production of the car: ")
        hp = input("Enter the hp of the car: ")
        cap = input("Enter the engine capacity of the car: ")
        color = input("Enter the color of the car: ")
        add(producer, model, type, year, hp, cap, color, user)
    if enter == "my account":
        dashboard(user)
    if enter == "Log out":
        user = 0


"""
- create account:
    - admin
    - customer
- log in:
    see my dashboard
- buy cars
- sell cars

"""
