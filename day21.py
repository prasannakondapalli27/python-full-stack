# CLASSES AND OBJECTS IN PYTHON
# CLASS, OBJECT, ATTRIBUTES, AND METHODS
class Student:
    # Constructor method
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    # Instance method
    def introduce(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
    # Instance method
    def study(self):
        print(self.name, "is studying", self.course)
# OBJECT CREATION
student1 = Student("Anita", 20, "Python")
student2 = Student("Rahul", 22, "Java")
student1.introduce()
student2.study()
#  ACCESSING AND CHANGING ATTRIBUTE
print(student1.name)
print(student1.age)
student1.age = 21
print(student1.age)
# self KEYWORD 
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def show_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
car1 = Car("Toyota", "Camry")
car1.show_details()
# STATIC METHODS 
class Calculator:
    @staticmethod
    def add(number1, number2):
        return number1 + number2
    @staticmethod
    def is_even(number):
        return number % 2 == 0
print(Calculator.add(10, 20))
print(Calculator.is_even(8))
#  CLASS ATTRIBUTE AND INSTANCE ATTRIBUTE 
class Employee:
    company = "Tech Solutions"  # Class attribute
    def __init__(self, name, salary):
        self.name = name        # Instance attribute
        self.salary = salary    # Instance attribute
    def show_details(self):
        print(self.name, self.salary, Employee.company)
employee1 = Employee("Meera", 50000)
employee2 = Employee("Arjun", 60000)
employee1.show_details()
employee2.show_details()