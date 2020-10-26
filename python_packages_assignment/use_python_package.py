"""
Program: use_python_package.py
Author: Grayson Hardin
Last date modified: 10/26/2020

This python package uses three files to output a list of messages.
"""


from python_packages_assignment.definitions import dictionary_ops, greeting, set_ops

dictionary_ops.print_dict(dictionary={'A:': 10, 'B:': 20, 'C:': 30})
greeting.greeting()
greeting.message()
set_ops.print_set(my_set={1, 2, 3})
