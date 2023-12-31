# using list comprehension to create a new list
# from an existing list of numbers and add 1 to it
numbers = [1, 2, 3, 4, 5]
# new_list = [new_item for item in list]
number_list = [number + 1 for number in numbers]
# new_number_list = [2, 3, 4, 5, 6]
print(number_list)

name = "Prerna"
letter_list = [letter for letter in name]
# new_list = ['P', 'r', 'e', 'r', 'n', 'a']
print(letter_list)

# create new list from range(1, 5) where
# numbers are doubled in the new list
range_list = [n * 2 for n in range(1, 5)]
print(range_list)

# Conditional List Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

# iterating rows in pandas data frame
import pandas

student_dict = {
    "student": ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"],
    "score": [54, 90, 78, 89, 34,62]
}
# print(student_dict)
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
# use method iterrows() to iterate rows in pandas data frame
for index, row in student_data_frame.iterrows():
    print(f"{row.student} {row.score}")
