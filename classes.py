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
