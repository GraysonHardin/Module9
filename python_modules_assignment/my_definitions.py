"""
Program: my_definitions.py
Author: Grayson Hardin
Last date modified: 10/26/2020

A list of functions that can be called in another file.
"""


def greeting():
    print("Hello, welcome!")


def message():
    author = 'Grayson Hardin'
    print('The author is', author)


def print_dict(dictionary):
    [print(key, value) for key, value in dictionary.items()]


def print_set(my_set):
    print('\n'.join(map(str, my_set)))





