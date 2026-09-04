# EXCEPTION HANDLING IN PYTHON
#try and except
try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Please enter a valid number")
#  Handling ZeroDivisionError
try:
    number1 = 10
    number2 = 0
    result = number1 / number2
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")
#  Handling Multiple Exceptions
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(result)
except ValueError:
    print("Invalid input. Enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero")
# Using one except for many errors
try:
    value = int(input("Enter a number: "))
    print(10 / value)
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero")
#else Block
try:
    number = int(input("Enter a number: "))
    result = 100 / number
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result:", result)
# finally Block
try:
    file = open("sample.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found")
finally:
    print("File operation completed")
#  Raising an Exception
age = 15
try:
    if age < 18:
        raise ValueError("Age must be 18 or above")
except ValueError as error:
    print(error)
# Custom ExceptiON
class InvalidMarksError(Exception):
    pass
def check_marks(marks):
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100")
    print("Valid marks:", marks)
try:
    check_marks(120)

except InvalidMarksError as error:
    print(error)