# region last lesson
# list1 = [1, 2, 3, 4, "hello"]
# string1 = "asdsad"
#
#
#
# # len_result = len(string1)
#
# # print(len_result)
#
#
# string1.upper()
# print(string1.upper())
# print(string1)
#
# print(list1)
# list1.append("hello world")
# print(list1)
#
#
# #
# # list1.append(1)
# #
# #
# # print(list1)
# #
# # MUTABLE
#
#
# # IMMUTABLE
# endregion

# region Joins and splits

# # .join()
# #
# # list1 = ["I", "really", "like", "pokemon"]
# # #
# # # print(list1)
# # #
# # combined = " ".join(list1)
# # #
# # print(combined)
#
#
# mishpat = "I really like pokemon"
#
# print(mishpat)
#
# splitted_mishpat = mishpat.split(" ")
#
# # print(splitted_mishpat)
#
# splitted_mishpat[-1] = "pizza"
#
# # print(splitted_mishpat)
#
# mishpat = " ".join(splitted_mishpat)
#
# print(mishpat)


# endregion


######## INTS FLOATS AND COMPLEX


# 12
#
# 5
#
# 109
#
# -3
#
# -0
#
#
# 3.12
# 5.4
#
# 3.1415926323
#
# 3.0
#
# print(3+3)
#
# print(2-1)
#
#
# # WE cant <"3" + 3>
#
# list1 = ["banana", "hello", "meow"]
#
#
# print("Length of list:")
# print(len(list1))
#
# print("Length of list if we append 10 times:")
# # len(list1) + 10
# print(len(list1) + 10)


# MATH OPERATIONS

# +
# -
# *
# /
# **
# //
# %
#
#
# print(3 + 3)
#
# print(2 - 1)
#
# print(3 * 3)
#
# print(9 / 2)
# print(9 / 3)
#
# print(2 ** 8) # חזקה
#
# print(9 // 2) # חילוק ללא שארית
#
# print(9 % 2)
# print(10 % 4)
#
# print(3.0 + 3.5)
#
# print(3.5 + 7)
# print(3.0 + 7)
#
# print(2.0 * 5)


# # we can turn floats back to ints (and vise versa)
#
# total = 10/5
# print(total)
#
# print(int(total))
#
# ###
#
# total = 10/5
# total = int(total)
# print(total)
#
# ###
#
# total = int(10/5)
# print(total)

# print(float(9))

# print(int(3.5))
# print(int(3.123))
# print(int(1231245153.13521356136236234623))

#####################################
# so far we learned about
# strings = str() (IMMUTABLE)
# lists = list()
# ints = int()
# floats = float()

# empty_list = list()

# float(5) = 5.0
# float("5.0") = 5.0



###################
# INPUT FUNCTION
# input will always return a string

# sentence = "Welcome! How are you"
#
# user_input = input("Please input your name:\n         - ")
#
# print(user_input + " The king!")


# STDIN by default is the Console
# STDOUT by default is the Console
# STDERR by default is the Console

# apples = input("How many apples you have? ")
#
# apples_as_int = int(apples)
#
# apples_after_i_ate_them = apples_as_int - 2
#
# print("I ate 2 apples! now you only have " + str(apples_after_i_ate_them))


# OPTION 2
# print("I ate 2 apples! now you only have " + str(int(input("How many apples you have? ")) - 2))

