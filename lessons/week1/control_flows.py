"""
Control flows are the ones responsible for the continuity of program execution

It dictates the arrangement and flow of the program
"""

# Asking input from terminal
number = input('Give a number:')
# The return of input is always a string, you need to typecast
number = int(number)

print(f"number is {number}")

# Logical operators
number > 0   
number < 0
number == 0

number is not 0
number != 0 # same as above

# Using "is" operator
number is not None
number is None

1 is not 0 # return true
1 is 0	# return false


# If else if example
if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
elif number == 0:
    print("Number is 0")
else:
    print("I dont know anymore")


# Shorthand assignment
num_sign = "positive" if number > 0 else "negative"
print(num_sign)


# Loops

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 1

# Remove comment to try
# Example of a while loop

#while i <= number:
#    print([x * i for x in nums])
#    i += 1      # i = i + 1


# Example of a for in loop

for n in range(1, number + 1):
   print([x * n for x in range(1, number + 1)])


# Example of a for - else usage

for n in range(100):
    if number == n:
        print(f"Found number: {n}")
        break
else:
    print("not found")


person = {
    "name": "ninz",
    "age": 18,
    "height": 5.6,
    "hobbies": ["music", "astronomy", "cooking"],
    "addresses": [
        {
            "street": 100,
            "brgy": "poblacion",
            "town": "tayabas"
        }
    ]
}

# Example of iterating to a dictionary

for key, value in person.items():
    print(f"The key is: {key}")
    print(f"The value is: {value}")
   
    #if key == 'hobbies':
    print(type(value))
    if type(value) == 'list':
        for hobby in value:
            print(f"My hobbies are {hobby}")
    




















