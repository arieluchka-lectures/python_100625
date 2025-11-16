# open("students.txt")
#
# if "os" == "Windows_NT":
#     path_to_file = "C:\\personal\\!obsidian_limudey_huts\\100625 (ramat gan)\\hangman_proj_2\\.gitignore"
# elif "os" == "linux":
#     path_to_file = "/personal/!obsidian_limudey_huts/100625 (ramat gan)/hangman_proj_2/.gitignore"




# file1 = open("greetings.txt", mode="r")
# file2 = open("greetings.txt", mode="r")

#
# # 4 lines
# # the forth word
# # word on index 4
# # 4 characters
# print(file.read(4))
# print(file.read(4))
# print(file.read(4))
#
# # When we are opening and read() a file, python remembers where we stopped

#
# file1 = open("greetings.txt", mode="r")
# file2 = open("greetings.txt", mode="r")
#
# print(file1.read(4))
# # print(file2.read(4))
#
#
# print(file1.read(8))
# # print(file2.read(1))
#
# # print(file.read(6))





# file1 = open("greetings.txt", mode="r")


# print(file1.readline())
# print(file1.readline())

# print(file1.read(5))
# print(file1.readlines())
# print(file1.read(192945193857))
#
# whole_file = file1.read(100)
# print(whole_file)


# list_maybe = whole_file.split(sep="\n")






# file1 = open("greetings.txt", mode="r")
# all_lines = file1.readlines()
# for l in all_lines:
#     print(l)

#OR

# file1 = open("greetings.txt", mode="r")
# for l in file1:
#     print(l)

#OR

# for l in open("greetings.txt", mode="r"):
#     print(l)


# ##############################################
#
# f = open("greetings.txt", mode="w")
# f.close()
# # Every time we open a file, we will close it with file.close()
#
# ##############################################
# f = open("greetings.txt", mode="w")
#
# f.write("line 1\n")
# f.write("line 2\n")
#
# f.close()
#
# ##############################################
#
# all_lines = open("greetings.txt", mode="r").readlines()
#
# f = open("greetings.txt", mode="w")
# for line in all_lines:
#     f.write(line)
#
# f.write("line 3\n")
#
# f.close()

##############################################

# f = open("greetings.txt", mode="a")
#
# f.write("line 1\n")
# f.write("line 2\n")
#
# f.close()

######
# echo "hello" >> file.txt
######

# f = open("greetings.txt", mode="a")
#
# (f.read(5))

##############################################
