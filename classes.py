class User():
    def __init__(self, username, name, surname, birthday, password, admin):
        self.username = username
        self.surname = surname
        self.name = name
        self.birthday = birthday
        self.password = password
        self.admin = admin

    def __str__(self):
        return self.username


class Car():
    def __init__(self, producer, model, type, year, hp, cap, color, owner):
        self.producer = producer
        self.model = model
        self.type = type
        self.year = year
        self.hp = hp
        self.cap = cap
        self.color = color
        self.owner = owner
