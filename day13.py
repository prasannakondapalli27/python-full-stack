# PYTHON SCOPE, PASS BY VALUE / REFERENCE, AND RECURSION
# SCOPE 
# 1. Local variable
def show_local():
    message = "This is a local variable"
    print(message)
show_local()
# 2. Global variable
name = "Anita"
def show_global():
    print(name)
show_global()
# 3. Changing a global variable
count = 0
def increase_count():
    global count
    count = count + 1
increase_count()
print(count)
# 4. Same local and global variable name
number = 100
def show_number():
    number = 50
    print(number)
show_number()
print(number)
#  PASS BY VALUE / REFERENCE
# Immutable values like integers cannot be changed outside the function
def change_number(number):
    number = 100
    print("Inside function:", number)
value = 10
change_number(value)
print("Outside function:", value)
# Mutable values like lists can be changed inside the function
def add_item(items):
    items.append("Python")
subjects = ["Java", "C"]
add_item(subjects)
print(subjects)
# Changing a list variable to a new list does not change the original list
def replace_list(items):
    items = ["HTML", "CSS"]
    print("Inside function:", items)
languages = ["Python", "Java"]
replace_list(languages)
print("Outside function:", languages)
# recursion
# 1. Countdown using recursion
def countdown(number):
    if number == 0:
        return
    print(number)
    countdown(number - 1)
countdown(5)
# 2. Factorial using recursion
def factorial(number):
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1)
print(factorial(5))
# 3. Sum of numbers using recursion
def sum_numbers(number):
    if number == 1:
        return 1
    return number + sum_numbers(number - 1)
print(sum_numbers(5))
# 4. Fibonacci series using recursion
def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)
for i in range(8):
    print(fibonacci(i))