# TYPES OF METHODS AND CONSTRUCTORS IN PYTHON OOP
# CONSTRUCTOR
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_details(self):
        print(self.name, self.age)
student1 = Student("Anita", 20)
student1.show_details()
#DEFAULT CONSTRUCTOR
class Welcome:
    def __init__(self):
        print("Welcome to Python")
welcome1 = Welcome()
# PARAMETERIZED CONSTRUCTOR
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def show_car(self):
        print(self.brand, self.model)
car1 = Car("Toyota", "Camry")
car1.show_car()
# INSTANCE METHOD
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def show_details(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
employee1 = Employee("Rahul", 50000)
employee1.show_details()
#  CLASS METHOD
class Product:
    tax_rate = 0.18
    def __init__(self, name, price):
        self.name = name
        self.price = price
    @classmethod
    def change_tax_rate(cls, new_tax_rate):
        cls.tax_rate = new_tax_rate
    def final_price(self):
        return self.price + (self.price * Product.tax_rate)
product1 = Product("Laptop", 50000)
print(product1.final_price())
Product.change_tax_rate(0.12)
print(product1.final_price())
#STATIC METHOD
class MathOperations:
    @staticmethod
    def add(number1, number2):
        return number1 + number2
    @staticmethod
    def is_even(number):
        return number % 2 == 0
print(MathOperations.add(10, 20))
print(MathOperations.is_even(8))
# DESTRUCTOR
class FileExample:
    def __init__(self, file_name):
        self.file_name = file_name
        print("Object created:", self.file_name)
    def __del__(self):
        print("Object destroyed:", self.file_name)
file1 = FileExample("notes.txt")
del file1