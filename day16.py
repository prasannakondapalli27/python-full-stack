# LIST COMPREHENSION, FILTERING, TRANSFORMING, AND NESTED LIST COMPREHENSION
# BASIC LIST COMPREHENSION
# Create a list of squares
numbers = [1, 2, 3, 4, 5]
squares = [number * number for number in numbers]
print(squares)
# Create a list from 1 to 10
numbers = [number for number in range(1, 11)]
print(numbers)
# FILTERING LISTS
# Get only even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)
# Get numbers greater than 10
numbers = [5, 12, 8, 20, 3, 15]
greater_numbers = [number for number in numbers if number > 10]
print(greater_numbers)
# Get names longer than 4 characters
names = ["Ram", "Anita", "John", "Priya", "Sam"]
long_names = [name for name in names if len(name) > 4]
print(long_names)
#  TRANSFORMING LISTS 
# Convert names to uppercase
names = ["ram", "anita", "priya"]
upper_names = [name.upper() for name in names]
print(upper_names)
# Add 10 to every number
numbers = [1, 2, 3, 4, 5]
new_numbers = [number + 10 for number in numbers]
print(new_numbers)
# Convert words to their lengths
words = ["Python", "Java", "C", "HTML"]
lengths = [len(word) for word in words]
print(lengths)
#  FILTERING AND TRANSFORMING 
# Square only even numbers
numbers = [1, 2, 3, 4, 5, 6]
even_squares = [number * number for number in numbers if number % 2 == 0]
print(even_squares)
# Convert long names to uppercase
names = ["Ram", "Anita", "John", "Priya", "Sam"]
upper_long_names = [name.upper() for name in names if len(name) > 4]
print(upper_long_names)
# Replace negative numbers with 0
numbers = [10, -5, 20, -3, 8]
positive_numbers = [number if number >= 0 else 0 for number in numbers]
print(positive_numbers)
#  NESTED LIST COMPREHENSION --------------------
# Flatten a nested list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [number for row in matrix for number in row]
print(flat_list)
# Create a 3 x 3 matrix
matrix = [[0 for column in range(3)] for row in range(3)]
print(matrix)
# Create coordinate pairs
pairs = [(x, y) for x in range(1, 4) for y in range(1, 4)]
print(pairs)
# Get even numbers from a nested list
numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
even_numbers = [number for row in numbers for number in row if number % 2 == 0]
print(even_numbers)