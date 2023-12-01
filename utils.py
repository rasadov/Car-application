from database import show_cars, show_car, add, dashboard
from classes import User


def buy():
    show_cars()
    enter = input("which car you wanna buy? ")
    show_car(enter)


def sell(user: User):
    producer = input("Enter the producer of the car: ")
    model = input("Enter the model of the car: ")
    type = input("Enter the type of the car (sedan, suv, sportcar,...): ")
    year = input("Enter the year of production of the car: ")
    hp = input("Enter the hp of the car: ")
    cap = input("Enter the engine capacity of the car: ")
    color = input("Enter the color of the car: ")
    a = user.__str__()
    add(producer, model, type, year, hp, cap, color, a)


def main(enter, user: User):
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


if __name__ == "__main__":
    a = User("dfsaf", "dsfj", "asd", 24, "fsfsdf", 1)
    print(a.username)
