from database import login, register, dashboard, add, username_exist, show_cars, show_car, userclass
from classes import User
import utils

enter = ""
user = 0

while (enter != "exit"):
    if user == 0:
        user = utils.check_user()
        if user == False:
            user = 0
            continue
        elif user == "exit":
            break
    if user.admin == 0:
        enter = input("""-Buy a car
-Sell a car
-My account
-Log out
""")
        utils.customer(enter, user)

    if user.admin == 1:
        enter = input("""
-Buy a car
-Sell a car
-My account
-Database
-Log out
""")
        utils.admin(enter, user)


"""
- create account: 1
    - admin and customer 0 
- log in: 1
    see my dashboard 1
- cart 0
- buy cars 1
- sell cars 1

"""
