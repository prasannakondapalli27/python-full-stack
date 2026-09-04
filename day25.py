# ENCAPSULATION IN PYTHON OOP
# PUBLIC ATTRIBUTE
class Student:
    def __init__(self, name):
        self.name = name
student = Student("Anita")
print(student.name)
student.name = "Rahul"
print(student.name)
# PROTECTED ATTRIBUTE
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
    def show_salary(self):
        print(self._salary)
employee = Employee("Meera", 50000)
employee.show_salary()
# Protected attributes can still be accessed,
# but they should not be accessed directly.
print(employee._salary)
#PRIVATE ATTRIBUTE
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance
    def show_balance(self):
        print("Balance:", self.__balance)
account = BankAccount("Anita", 10000)
account.show_balance()
# This will cause an error:
# print(account.__balance)
# Name mangling can access it, but should be avoided:
print(account._BankAccount__balance)
# GETTER AND SETTER METHODS
class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price
    def get_price(self):
        return self.__price
    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Price must be greater than zero")
product = Product("Laptop", 50000)
print(product.get_price())
product.set_price(45000)
print(product.get_price())
product.set_price(-100)
#@property DECORATOR 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, new_age):
        if new_age >= 0:
            self.__age = new_age
        else:
            print("Age cannot be negative")
person = Person("Rahul", 20)
print(person.age)
person.age = 25
print(person.age)
person.age = -5