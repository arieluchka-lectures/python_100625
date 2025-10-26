#data types

#variables


"Ariel"

#name = "yakov"
#hello = "My name is"

#print(hello + name)


##########
# sequence
##########

#### STRINGS ####
"Ariel"
'Ariel'

#print('Hello\n\n\n\n\nWorld')

#"abcd" + "efgh"

# = "abcdefgh"


my_string = "hello world i like ice cream"
#            0123456  .....             27
# INDEX
# We are counting the index from 0

# my_string[N]

# if i want to print "d"
#print(my_string[10])




# my_string[N:M] (NOT INCLUDING M!)

#print(my_string[0:5])
#print(my_string[:5])


#print(my_string[5:8])


#print(my_string[10:28]) # -> "m" is on index 27, so we need to print until 28 (not including 28)

#print(my_string[10:])

#print(my_string[:])




# my_string[N:M:X]

#print(my_string[6:28:2])

# how can we get the same result with less code?
#print(my_string[6::2])

#print(my_string[3:16:3])

#print the whole string, but only every 3 characters
#print(my_string[::3])



# COUNT FROM THE END
#print(my_string[-1])

#print(my_string[-5])


#e=-7
#print(my_string[6:-6])
#print(my_string[6:-7])


#print(my_string[::-1])

#print(my_string[10:5:-1])






#########################
# raz question
# how ranges will behave, if we use special characters?
#
#
#example = "hello\nworld"
#          0123456789...

#print(example[0:5])
#print(example[0:6])
#print(example[0:7])

#########################















#### Lists ####

# INDEXING
#my_list = ["hello", "ariel", 8, 12, "banana", "israel"]
#           0         1     2

#print(my_list)

#print(my_list[0])
#print(my_list[2])
#print(my_list[-1])
#print(my_list[0:2])
#print(my_list[0:5:2])


# we want to display "hello" backwards.

# word = my_list[0]

# print(word[::-1])


# print(my_list[0][::-1])






# Methods
my_list = ["hello", "ariel", 8, 12, "banana", "israel"]


# the function len()
#list_length = len(my_list)

#print(list_length)

###

#my_list.append("shahar")

#print(my_list)

#my_list.append(7)

#print(my_list)

#my_list.append(["hello", "shahar"])

#print(my_list)



#my_list.append("shahar")

#print(my_list)


#new_list = [my_list[0], my_list[-1], my_list[1:6]]


#print(new_list)





# LISTS ARE MUTABLE


example = [1, 2, 3]
print(example)


example.append(4)

print(example)


example[1] = "banana"


print(example)







# Create a new empty list and append to it at least three names of students.
#[]



#[NAME1, NAME2, NAME3]


new_list.extend([])




new_list.extend()

new_list.extend("banana")

new_list.append("b")
new_list.append("a")
new_list.append("n")
new_list.append("a")
new_list.append("n")
new_list.append("a")





















#### tuples ####

#### dict (dictionary) ####






























###################################
# functions and methods
###################################

# FUNCTIONS

# print("hello world")


#
# def print():
#     ...

# print("ariel")
#
# def ariels_name(given_name):
#     print("1 + 1 = ")
#     print(1+1)
#
#     print("my name is")
#     print(given_name)


# ariels_name(given_name="ariel")
# ariels_name(given_name="shahar")













# city_name = "Rehovot"
#
# the_len_of_the_city = len(city_name)
#
# print(the_len_of_the_city + 5)
# print(len(city_name))
#
# print(len("hello class!                   "))

















# METHODS


# name = "ariel".upper()
#
# ["1", "2", "3"].

# print(name)
# print





# non-sequence
































