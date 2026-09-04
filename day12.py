# FUNCTIONS IN PYTHON
# 1. Simple function
def greet():
    print("Hello, welcome!")

greet()
# 2. Function with parameters
def greet_user(name):
    print("Hello", name)

greet_user("Anita")
# 3. Function with two parameters
def add(a, b):
    print(a + b)

add(10, 20)
# 4. Function with return value
def multiply(a, b):
    return a * b

result = multiply(5, 4)
print(result)
# 5. Function to check even or odd
def check_even_odd(number):
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

check_even_odd(7)
# 6. Function with default parameter
def introduce(name, city="Delhi"):
    print(name, "lives in", city)

introduce("Rahul")
introduce("Meera", "Mumbai")
# 7. Function to find the largest number
def find_largest(a, b):
    if a > b:
        return a
    else:
        return b

print(find_largest(10, 25))
# 8. Function to calculate factorial
def factorial(number):
    fact = 1

    for i in range(1, number + 1):
        fact = fact * i

    return fact

print(factorial(5))
# 9. Recursive function
def countdown(number):
    if number == 0:
        return
    print(number)
    countdown(number - 1)

countdown(5)
# 10. Function with a list
def show_numbers(numbers):
    for number in numbers:
        print(number)

show_numbers([10, 20, 30, 40])