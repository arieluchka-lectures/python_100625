# Exercise 1: Comparing strings
from traceback import print_tb

favorite_color = "blue"
# Write an if statement that prints "We have the same favorite color!" if favorite_color equals "blue"


# Exercise 2: if-else statement
temperature = 25
# Write an if-else statement that prints "Hot day" if temperature is above 30, otherwise print "Nice weather"


# Exercise 3: Checking list length
my_list = [1, 2, 3, 4, 5]
# Write an if statement that prints "List has more than 3 items" if the length of my_list is greater than 3


# Exercise 4: if-elif-else chain
score = 85
# Write an if-elif-else statement:
# - Print "Excellent" if score is 90 or above
# - Print "Good" if score is between 70 and 89
# - Print "Needs improvement" if score is below 70


# Exercise 5: Multiple conditions with 'and'
# Write an if statement that prints "Access granted" only if username is "admin" AND password is "1234"
username = "admin"
password = "1234"

#username = "admin"
#password = "qwerty"

#username = "user"
#password = "1234"


# Exercise 6: Multiple conditions with 'or'
day = "Saturday"
# Write an if statement that prints "It's the weekend!" if day is "Saturday" OR "Friday"



# Exercise 7: Checking if item in list
fruits = ["apple", "banana", "orange", 1, 2, 5]
# Write an if statement that prints "We have 2!" if 2 is in the fruits list
#
# if 2 in fruits:


# Exercise 8: String contains substring
sentence = "I love programming in PytHoN"
# Write an if statement that prints "Python mentioned!" if the word "Python" is in the sentence

if "python" in sentence.lower():
    print("Python mentioned!")


# Exercise 9: Negative numbers
number = -5
# Write an if-else statement that prints "Negative" if number is less than 0, otherwise print "Positive or zero"


# Exercise 10: Even or odd
num = 17
# Write an if-else statement that prints "Even" if num is divisible by 2 (use % operator),
# otherwise print "Odd"

# + - / * **

# //
# %


# 1)
# if num % 2 > 0:
#     print("Odd")
# else:
#     print("Even")
#
#
# # 2)
# if num % 2 > 0:
#     print("Odd")
# elif num % 2 == 0:
#     print("Even")

# 3)
# if num % 2 != 0:
#     print("Odd")
# ...

# 4)
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# 5)

if num % 2:
    print("Odd")
else:
    print("Even")



# Exercise 11: String length check
name = "Alexander"
# Write an if statement that prints "Long name" if the length of name is more than 7 characters


# Exercise 12: Comparing two numbers
x = 10
y = 20
# Write a conditional statement that prints:
# - "x is greater" if x > y
# - "y is greater" if y > x
# - "They are equal" if x == y


# Exercise 13: Nested if statements
is_raining = True
has_umbrella = False
# Write nested if statements:
# - If it's raining, check if has_umbrella is True
#   - If True, print "You can go out safely"
#   - If False, print "You'll get wet"
# - If it's not raining, print "Enjoy your day"


# Exercise 14: Empty list check
shopping_cart = []
# Write an if-else statement that prints "Cart is empty" if shopping_cart has no items, otherwise print "You have items in cart"


# Exercise 15: Price discount
price = 150
# Write an if-else statement:
# - If price is more than 100, calculate 10% discount and print the new price
# - Otherwise, print the original price

# Exercise 16: Grade calculator
grade = 78
# Write a conditional statement chain that prints:
# - "A" if grade is 90-100
# - "B" if grade is 80-89
# - "C" if grade is 70-79
# - "D" if grade is 60-69
# - "F" if grade is below 60


# Exercise 17: String starts with
word = "Python"
# Write an if statement that prints "Starts with P" if word starts with the letter "P" (capital "p")


# Exercise 18: List contains specific number
numbers = [5, 10, 15, 20, 25]
# Write an if-else statement that prints "Found 15" if 15 is in numbers, otherwise print "Not found"


# Exercise 19: Multiple conditions combined
student_age = 16
has_permission = True
# Write an if statement that prints "Can attend" if student_age is *at least* 16 AND has_permission is True


# BONUS Exercise 20: Complex conditions
height = 165
weight = 70
# Write an if-elif-else statement:
# - Print "Tall and heavy" if height > 180 AND weight > 80
# - Print "Average" if height is between 160-180 OR weight is between 60-80
# - Print "Other category" for all other cases