# INHERITANCE IN PYTHON OOP
# SINGLE INHERITANCE
class Animal:
    def eat(self):
        print("Animal eats food")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
dog = Dog()
dog.eat()
dog.bark()
# USING super()
class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course
    def show_details(self):
        print("Name:", self.name)
        print("Course:", self.course)
student = Student("Anita", "Python")
student.show_details()
# MULTILEVEL INHERITANCE
class Grandparent:
    def house(self):
        print("Grandparent has a house")
class Parent(Grandparent):
    def car(self):
        print("Parent has a car")
class Child(Parent):
    def bike(self):
        print("Child has a bike")
child = Child()
child.house()
child.car()
child.bike()
# MULTIPLE INHERITANCE
class Father:
    def skills_from_father(self):
        print("Father: Driving")
class Mother:
    def skills_from_mother(self):
        print("Mother: Cooking")
class Child(Father, Mother):
    def own_skill(self):
        print("Child: Programming")
child = Child()
child.skills_from_father()
child.skills_from_mother()
child.own_skill()
# HIERARCHICAL INHERITANCE
class Employee:
    def work(self):
        print("Employee works")
class Developer(Employee):
    def code(self):
        print("Developer writes code")
class Tester(Employee):
    def test(self):
        print("Tester tests software")
developer = Developer()
tester = Tester()
developer.work()
developer.code()
tester.work()
tester.test()