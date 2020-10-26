"""
Program: use_my_definitions.py
Author: Grayson Hardin
Last date modified: 10/26/2020

A file uses functions from another file and prints them to the console.

"""


from python_modules_assignment.my_definitions import greeting, message, print_set, print_dict

greeting()
message()
print_dict(dictionary={'A:': 10, 'B:': 20, 'C:': 30})
print_set(my_set={1, 2, 3})
