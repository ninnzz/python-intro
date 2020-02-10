"""
Python has a weak typing check (weakly typed language)
Follows duck typing (it quacks)

Variable type is "interpreted" on run time
"""


# Strings
name = 'Ninz'

# Integers
number = 1

# Boolean
true_value = True

# Float
decimal = 3.14

# Byte string
byte_string = b'this is a byte string'



age = 18
height = 5.6

# Using f-string to print
print(f"My name is {name}, age {age}, height {height}")

# Defining a function
def print_age(n):
    return n + 10

# f-string allows code evaluation as well
print(f"In 10 years I will be {print_age(age)} years old.")
