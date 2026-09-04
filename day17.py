# MODULES IN PYTHON
# BUILT-IN MODULES
# math module
import math
print(math.sqrt(25))
print(math.factorial(5))
print(math.pi)
# random module
import random
print(random.randint(1, 10))
print(random.choice(["Python", "Java", "C"]))
# datetime module
import datetime
today = datetime.date.today()
print(today)
#  IMPORTING SPECIFIC ITEMS
from math import sqrt, factorial
print(sqrt(16))
print(factorial(4))
# IMPORTING WITH AN ALIAS
import math as m
print(m.sqrt(49))
#USER-DEFINED MODULE
def greet(name):
    print("Hello", name)
def add(a, b):
    return a + b