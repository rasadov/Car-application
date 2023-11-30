import pandas as pd
import csv

from classes import User

users = pd.read_csv("users.csv")
database = pd.read_csv("database.csv")


def add(producer, model, type, year, hp, cap, color, user):
    with open('database.csv', 'a', newline='') as storage2:
        csv_writer = csv.writer(storage2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(
            (producer, model, type, year, hp, cap, color, user))
    database = pd.read_csv("database.csv")
    print("Success")


def register(username, name: None, surname: None, birthday: None, password):
    if username in users["username"]:
        print("this username is already being used.")
        return 0
    if len(password) < 8:
        print("password is too short.")
        return 0
    with open('users.csv', 'a', newline='') as storage2:
        csv_writer = csv.writer(storage2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)

        csv_writer.writerow((username, name, surname, birthday, password))


def login(username, password):
    if len(users.loc[users["username"] == username]) == 1:
        if len(users.loc[(users["username"] == username) & (users["password"] == password)]) == 1:
            return 1
    else:
        username = 0
        print("No such account")
    return 0


def dashboard(username):
    database = pd.read_csv("database.csv")
    users = pd.read_csv("users.csv")
    user = users.loc[users["username"] == "baddd"]
    user = User(*[i for i in user.values[0]])
    print(f"Good day {user.name} {user.surname}")
    print("Your listings:")
    print(database.loc[database["owner"] == username,
                       ["producer", "model", "type", "year", "hp", "cap", "color"]])


def username_exist(username):
    users = pd.read_csv("users.csv")
    if len(users.loc[users["username"] == username]) == 1:
        return True
    return False


def show_cars():
    database = pd.read_csv("database.csv")
    print(database)


def show_car(car):
    users = pd.read_csv("users.csv")
    database = pd.read_csv("database.csv")
    owner = database.iloc[int(car)]["owner"]
    user = users.loc[users["username"] == owner]
    user = User(*[i for i in user.values[0]])
    print(user.name, user.surname)


if __name__ == "__main__":
    user = users.loc[users["username"] == "baddd"]
    user = User(*[i for i in user.values[0]])
