# Reading a File


# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# now we don't have to manually close the file
# python will itself close the file when it's done
with open("../my_file.txt") as file:
    contents = file.read()
    print(contents)


# Writing to a file


# by default the file mode is read only
# to write in the file we need to change the mode to 'w'
# all the data will be overwritten
# with open("my_file.txt", mode="w") as file:
#     file.write("New text overwritten")
#     print(contents)

# to append in the file we need to change the mode to 'a'
# so that all the data will not be overwritten
with open("../my_file.txt", mode="a") as file:
    # to write in new line, add new line character
    file.write("\nNew text appended on a new line")


# if no such file exits, python is going to create it for you
# this only works in "w" or "a" mode only
with open("../new_file.txt", mode="a") as file:
    # to write in new line, add new line character
    file.write("\nNew text appended on a new line")



