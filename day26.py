# DATA ABSTRACTION IN PYTHON OOP
from abc import ABC, abstractmethod
# ABSTRACT CLASS
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("Cat meows")
dog = Dog()
cat = Cat()
dog.sound()
cat.sound()
# Animal() cannot be created because it has an abstract method.
# animal = Animal()
# ABSTRACT METHOD WITH PARAMETERS
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
rectangle = Rectangle(10, 5)
circle = Circle(7)
print(rectangle.area())
print(circle.area())
#  ABSTRACTION IN A BANK ACCOUNT
class BankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass
    @abstractmethod
    def withdraw(self, amount):
        pass
class SavingsAccount(BankAccount):
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited:", amount)
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")
    def show_balance(self):
        print("Balance:", self.balance)
account = SavingsAccount(10000)
account.deposit(2000)
account.withdraw(3000)
account.show_balance()