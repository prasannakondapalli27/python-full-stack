from functools import reduce
# filter()
# Example 1: Get even numbers
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
print(even_numbers)
# Example 2: Get names with more than 4 characters
names = ["Ram", "Anita", "John", "Priya"]
long_names = list(filter(lambda name: len(name) > 4, names))
print(long_names)
#map()
# Example 1: Square each number
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda number: number * number, numbers))
print(squares)
# Example 2: Convert names to uppercase
names = ["ram", "anita", "priya"]
upper_names = list(map(lambda name: name.upper(), names))
print(upper_names)
# reduce() 
# Example 1: Find the sum of all numbers
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda a, b: a + b, numbers)
print(total)
# Example 2: Find the product of all numbers
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda a, b: a * b, numbers)
print(product)
# Example 3: Find the largest number
numbers = [10, 25, 8, 40, 15]
largest = reduce(lambda a, b: a if a > b else b, numbers)
print(largest)