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
        enter = input("""
-Buy
-Sell
-Card
-My account
-Exit
""")
        utils.customer(enter, user)

    if user.admin == 1:
        enter = input("""
-Buy
-Sell
-My account
-Dashboard
-Database
-exit
""")
        utils.admin(enter, user)
