import pandas as pd
import csv


users = pd.read_csv("users.csv")
database = pd.read_csv("database.csv")


def add(producer, model, type, year, hp, cap, color):
    with open('database.csv', 'a', newline='') as storage2:
        csv_writer = csv.writer(storage2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)

        csv_writer.writerow((producer, model, type, year, hp, cap, color))


def register(username, name: None, surname: None, birthday: None, password):
    if username in users["username"]:
        print("this username is already being used.")
        return 0
    if len(password) < 8:
        print("password is too short.")
        return 0
    with open('database.csv', 'a', newline='') as storage2:
        csv_writer = csv.writer(storage2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)

        csv_writer.writerow(username, name, surname, birthday, password)


def login(username, password):
    if len(users.loc[users["username"] == username]) == 1:
        if len(users.loc[(users["username"] == username) & (users["password"] == password)]) == 1:
            return username
    else:
        print("No such account")
    return 0


def dashboard(username):
    user = users.loc[users['username'] == username]
    print(f"Good day {user['name'][0]} {user['surname'][0]}")
    print("Your listings:")
    print(database.loc[database["owner"] == username,
          ["producer", "model", "type", "year", "hp", "cap", "color"]])


if __name__ == "__main__":
    df = pd.read_csv("database.csv")
    print(df.iloc[1]["producer"])
