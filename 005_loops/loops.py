from urllib3 import proxy_from_url

# # if  5 < x < 10:
#
# if x == 5:
#     print("X is actually a 5!")
# elif x == 7:
#     print("X is actually a 7!")
# else:
#     ...




# LOOPs



# if 17.06:
    # copy all names
    # ...

# if 24.06:
    # copy all names

# import time


# starting_time = time.time()
# print("before the loop")
#
# count = 1000
#
# while count != 0:
#     print("hello! my name is ariel!")
#
#     count = count - 1
#     # count -= 1
#
#     # count = count + 1
#     # count += 1
#
#
# print("after the loop")
# asd = 10
# end_time = time.time()
# delta_time = end_time - starting_time

# print("The code ran in ", delta_time, "seconds")

# while <CONDITION>:
#     executing code until CONDITION is false


# while <TIME IS NOT ZERO>:
#     WAIT FOR A SECOND.


#
# time.time()
# time.sleep()



# FOR LOOPS

#
# for _ in ...:
#     ...
#

# sentence = "I like python"
#
# for character in sentence:
#     new_char = "!" + character + "?"
#     print(character)
#     print(new_char)


AVAILABLE_USERNAMES = ["arieluchka", "Ido", "Maryam"]
AVAILABLE_PASSWORDS = ["ariel111", "ido_the_king_1980", "01234"]


# "username=password"
# "arieluchka=ariel111"
#
# usernames_passwords_combined = ["arieluchka=ariel111", "Ido=ido=the=king_1980", "Maryam=01234"]
#
# res = usernames_passwords_combined[0].split("=")

# OBJ1 = ["arieluchka", "ariel111"]
# OBJ2 = ["Ido", "ido_the_king_1980"]
# OBJ3 = ["Maryam", "01234"]
#
#
# USERNAMES_WITH_PASSWORDS = [OBJ1, OBJ2, OBJ3]
#

USERNAMES_WITH_PASSWORDS = [
    ["arieluchka", "ariel111"],
    ["Ido", "ido_the_king_1980"],
    ["Maryam", "01234"],
]

print("Welcome to the computer")
# while until correct username and password

username_from_input = input("enter your username: ")
# username_exists = False


for X in USERNAMES_WITH_PASSWORDS:
    ...

if username_from_input in AVAILABLE_USERNAMES:
    print("username exists")
    password_from_input = input("enter your password: ")
    # username_exists = True

    if password_from_input in AVAILABLE_PASSWORDS:
        print("password exists")
    else:
        print("password is incorrect.")

else:
    print("username is incorrect. try again!")











