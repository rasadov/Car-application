from classes import User
import database


def buy():
    database.show_cars()
    enter = input("which car you wanna buy? ")
    database.show_car(enter)


def sell(user: User):
    producer = input("Enter the producer of the car: ")
    model = input("Enter the model of the car: ")
    type = input("Enter the type of the car (sedan, suv, sportcar,...): ")
    year = input("Enter the year of production of the car: ")
    hp = input("Enter the hp of the car: ")
    cap = input("Enter the engine capacity of the car: ")
    color = input("Enter the color of the car: ")
    a = user.__str__()
    database.add(producer, model, type, year, hp, cap, color, a)


def main(enter, user: User):
    if enter == "buy a car":
        database.show_cars()
        enter = input("which car you wanna buy? ")
        database.show_car(enter)
    if enter == "sell a car":
        producer = input("Enter the producer of the car: ")
        model = input("Enter the model of the car: ")
        type = input("Enter the type of the car (sedan, suv, sportcar,...): ")
        year = input("Enter the year of production of the car: ")
        hp = input("Enter the hp of the car: ")
        cap = input("Enter the engine capacity of the car: ")
        color = input("Enter the color of the car: ")
        database.add(producer, model, type, year, hp, cap, color, user)
    if enter == "my account":
        database.dashboard(user)
    if enter == "Log out":
        user = 0


def check_user():
    enter = input("log in or register? ")
    if enter == "exit":
        return "exit"
    elif enter == "log in":
        # global user
        user = input("Enter username ")
        password = input("Enter password ")
        ans = database.login(user, password)
        if (ans == 0):
            print("Incorrect username or password")
            user = 0
            return False

    elif enter == "register":
        # global user
        user = input("Create a username: ")
        if database.username_exist(user) == False:
            passwordofuser = input("Create a password: ")
            while len(passwordofuser) < 8:
                passwordofuser = input("It should be 8 characters minimum: ")
            nameofuser = input("Enter name ")
            surnameofuser = input("Enter surname ")
            bdofuser = input("Enter birthday ")
            database.register(user, nameofuser, surnameofuser,
                              bdofuser, passwordofuser)
            print("New account registrated")
            user = 0
            return False
        else:
            print("This username is already taken")
            user = 0
            return False
    else:
        print("No such command")
        return "exit"

    if type(user) != str:
        return False
    if database.username_exist(user) != True:
        print("first you have to log in")
        user = 0
        return False
    return database.userclass(user)


if __name__ == "__main__":
    a = User("dfsaf", "dsfj", "asd", 24, "fsfsdf", 1)
    print(a.username)
