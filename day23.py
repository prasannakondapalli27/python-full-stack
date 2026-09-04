# POLYMORPHISM IN PYTHON
#SAME METHOD, DIFFERENT OBJECTS 
class Dog:
    def sound(self):
        print("Dog barks")
class Cat:
    def sound(self):
        print("Cat meows")
animals = [Dog(), Cat()]
for animal in animals:
    animal.sound()
#FUNCTION POLYMORPHISM
def make_sound(animal):
    animal.sound()
dog = Dog()
cat = Cat()
make_sound(dog)
make_sound(cat)
#METHOD OVERRIDING
class Animal:
    def sound(self):
        print("Animal makes a sound")
class Cow(Animal):
    def sound(self):
        print("Cow moos")
class Lion(Animal):
    def sound(self):
        print("Lion roars")
animals = [Cow(), Lion()]
for animal in animals:
    animal.sound()
#BUILT-IN POLYMORPHISM
print(len("Python"))
print(len([1, 2, 3, 4]))
print(len({"name": "Anita", "age": 20}))
#OPERATOR POLYMORPHISM
print(10 + 20)
print("Hello" + " Python")
print([1, 2] + [3, 4])
#  POLYMORPHISM WITH SHAPES 
class Shape:
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
shapes = [Rectangle(10, 5), Circle(7)]
for shape in shapes:
    print(shape.area())