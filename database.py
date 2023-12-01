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
    # else:
        # username = 0
    return 0


def dashboard(user: User):
    database = pd.read_csv("database.csv")
    listings = database.loc[database["owner"] == user.username]
    if listings.empty:
        print(f"\nGood day {user.name} {user.surname}")
        print("You have no listings")
        print()
        return
    database = database.loc[database["owner"] == user.username]
    print(f"{user.name} {user.surname}\n")
    print(f"birthday: {user.birthday}")

    print("Your listings:")
    print(database[["producer", "model", "type", "year", "hp", "cap", "color"]])
    return database


def username_exist(username: str):
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


def userclass(user):
    users = pd.read_csv("users.csv")
    info = users.loc[users["username"] == user]
    return User(*[i for i in info.values[0]])


def remove_car(index, path):
    with open(path, 'r') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)
    if 0 <= index < len(data):
        # Delete the specified row
        del data[index]

        with open(path, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(data)
        print(f"Row at index {index} deleted successfully.")
    else:
        print(f"Invalid row index: {index}")


def remove_user(index, path, pathd):
    data = pd.read_csv(path)
    database = pd.read_csv("database.csv")
    if 0 <= index < len(data):
        # Delete the specified row
        name = data.iloc[index].values[0]
        database = database.loc[database["owner"] != name]
        data = data.drop(index)
        data.to_csv('users.csv', sep=',', index=False)
        database.to_csv(pathd, sep=',', index=False)
        print(f"Row at index {index} deleted successfully.")
    else:
        print(f"Invalid row index: {index}")


def edit_user(index, path):
    with open(path, 'r') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)
    if 0 <= index < len(data):
        # Delete the specified row
        del data[index]

        with open(path, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(data)
        print(f"Row at index {index} deleted successfully.")
    else:
        print(f"Invalid row index: {index}")


if __name__ == "__main__":
    user = users.loc[users["username"] == "baddd"]
    user = User(*[i for i in user.values[0]])
