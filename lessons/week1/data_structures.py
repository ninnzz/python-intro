"""
Data Structures are ways of arranging and organizing data to make operations more efficient
Data Structures provide ways of solving problems easier

There are many types of data structures that can be applied to solve specific problems
"""

fruits = ["apple", "banana", "atis", "santol", "pineapple"]

print(fruits)

# Print first
print(f"First fruit is {fruits[0]}")
print(len(fruits))

# Gets the length of fruits
l = len(fruits)
print(fruits[l-1])

# Print last item
print(fruits[-1])

# Printing sliced elements
print(fruits[1:3])

num = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10]

# List multiplication
print(num * 2)

letters = ['A', 'B']

# Adding two list together
print(num + letters)

# Example of list comprehension
print([x * 2 for x in num])

name = ['ben', 'carlo', 'juan', 'maria']
print([s.title() for s in name])



# Dictionary Implementation

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

print(f"My name is {person['name']}")

print(f"My last hobby is {person['hobbies'][-1]}")

print(person['addresses'][0]['town'])

# Assigning a new value
person['addresses'][0]['town'] = 'Lucena'
print(person)

# Assigning a new value
fruits[-1] = 'Grapes'
print(fruits)

















