# RECURSIVE FUNCTIONS & PASS BY VALUE / REFERENCE IN PYTHON
#recursive functions
# 1. Countdown
def countdown(number):
    if number == 0:
        return
    print(number)
    countdown(number - 1)
countdown(5)
# 2. Factorial
def factorial(number):
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1)
print(factorial(5))
# 4. Fibonacci number
def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)
for i in range(8):
    print(fibonacci(i))
# 5. Reverse a string using recursion
def reverse_text(text):
    if len(text) <= 1:
        return text
    return text[-1] + reverse_text(text[:-1])
print(reverse_text("Python"))
# pass by value
# Python passes object references to functions.
# Immutable objects (int, float, str, tuple) cannot be changed in place.
def change_number(number):
    number = 100
    print("Inside function:", number)
value = 10
change_number(value)
print("Outside function:", value)
# Mutable objects (list, dictionary, set) can be changed in place.
def add_subject(subjects):
    subjects.append("Python")
course_list = ["Java", "C"]
add_subject(course_list)
print(course_list)
# Changing a list variable to a new list does not affect the original list.
def replace_list(items):
    items = ["HTML", "CSS"]
    print("Inside function:", items)
languages = ["Python", "Java"]
replace_list(languages)
print("Outside function:", languages)
# Dictionary example: modifying it affects the original dictionary.
def add_city(student):
    student["city"] = "Delhi"
details = {"name": "Anita", "age": 20}
add_city(details)
print(details)