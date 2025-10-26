#
# print("hello world")
#
# if True:
#     print("hello world")
#
# if False:
#     ...

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



# Exercise 3: Checking list length
my_list = 90.12
# Write an if statement that prints "List has more than 3 items" if the length of my_list is greater than 3
# if it isnt greater than 3, print "The list doesnt have more than 3 items"

#
# list()
#
# int()
#
# input()

# type()


if type(my_list) == list:
    print("This is a list!")
    if len(my_list) > 3: # will check len only if this is actually a list
        print("List has more than 3 items")
    else:
        print("The list doesnt have more than 3 items")

else:
    print("This is not a list!")









