from database import login, register, dashboard, add


enter = input("login or register? ")

while (enter != "exit"):
    if enter == "login":
        user = input("Enter username ")
        password = input("Enter password ")
        ans = login(user, password)
        if (user != 0):
            dashboard(user)
    break

"""
- create account:
    - admin
    - customer
- log in:
    see my dashboard
- buy cars
- sell cars

"""
