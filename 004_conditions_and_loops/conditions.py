#
# print("hello world")
#
# if True:
#     print("hello world")
#
# if False:
#     ...
from idna.idnadata import scripts

# int + float + string + list + bool (True/False)

# temprature = 30
#
# temp_condition = temprature > 28
#
# if temp_condition:
#     print("today is a hot day")

#####

# string1 = "hello my name is ariel"
#
# if "itzhak" in string1:
#     print("my name is in the string!")

# list_1 = [1, 2, "hello", "cat", 52, 12.9, 1, 1, 1]
#
# if 42 in list_1:
#     print("the number 42, is in the list")


# נוכחות

# list_of_students_in_zoom = ["סרגיי", "יצחק", "אריאל", "מרים", "רגב"]
# list_of_all_students = ["מרים", "רגב", "עדן", "אריאל", "", "", "", "", ""]
# #                         0       1       2      3
# student_index = 2
#
# if list_of_all_students[student_index] in list_of_students_in_zoom:
#     print("The student " + list_of_all_students[student_index] + " is in the zoom!")
# else:
#     print("The student " + list_of_all_students[student_index] + " is NOT in the zoom!")


#t a list!")

# # Exercise 3: Checking list length
# my_list = [1, 2, 3, 4]
# # Write an if statement that prints "List has more than 3 items" if the length of my_list is greater than 3
# # if it isnt greater than 3, print "The list doesnt have more than 3 items"
#
# #
# # list()
# #
# # int()
# #
# # input()
#
# # type()
#
#
# if type(my_list) == list:
#     print("This is a list!")
#     if len(my_list) > 3: # will check len only if this is actually a list
#         print("List has more than 3 items")
#     else:
#         print("The list doesnt have more than 3 items")
#
# else:
#     print("This is no





# Exercise 4: if chain
# score = 85
# - Print "You got the maximum score" if score is 100
# - Print "Excellent" if score is 90 or above
# - Print "Good" if score is between 70 and 89
# - Print "Needs improvement" if score is between 70 and 55
# - Print "Failed" if score is below 55
# - Print "Terrible, we need to talk" if score is below 10


# 1.1)
# if score > 90 or score == 90:
#     ...

# 1.2)
# if score >= 90:
#     print("Excellent")

# 1.3) (not recommended)
# if score > 89:
#     ...


# 2.1)
# if score >= 70 and score <= 89:
#     print("Good")

# # 2.2)
# if score > 69 and score < 90:
#     print("Good")

# # 2.3)
# if score >= 70:
#     if score <= 89:
#         print("Good")

# if score < 70:
#     print("Needs improvement")


# 4)
# if score >= 90:
#     print("Excellent")
# else:
#     if score >= 70 and score <= 89:
#         print("Good")
#     else:
#         if score < 70 and score >= 55:
#             print("Needs improvement")
#         else:
#             print("Failed")

# 4.1)
# if score >= 90:
#     print("Excellent")
# elif score >= 70 and score <= 89:
#     print("Good")
# elif score < 70 and score >= 55:
#     print("Needs improvement")
# else:
#     print("Failed")

# score = 85

# 4.2)
# if score >= 90:
#     print("Excellent")
# elif score >= 55:
#     print("...")
# elif score >= 70:
#     print("Good")
# else:
#     print("Failed")

# when we have an if block (if/elif/else), only one block will execute

# if ...:
#     ...
# else:
#     ...

# if ...:
#     ...
# elif ...:
#     ...
# else:
#     ...



# first CONDITION block
# if 1 > 0:
    # print("...")
# else:
#     print("some other stuff")

# second CONDITION block
# if 5 > 12:
#     print("...")

# third CONDITION block
# if 5>12:
#     ...
# elif 10>50:
#     ...
# elif 5>5:
#     ...
# else:
#     ...








#####
# raz question
fruits = [
    "apple something",
    "banana",
    "orange",
    1,
    2,
    5,
    ["hello", "ariel"],
    3,
    10
]




if "apple" in fruits:
    print("apple in fruits?!")

if "ariel" in fruits:
    print("ariel in fruits?!")





