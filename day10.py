# NUMBER PROGRAMS USING LOOPS
# 1. Reverse a number
number = 1234
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

print("Reversed number:", reverse)  
# 2. Check palindrome number
number = 121
original = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

if original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome number")
# 3. Sum of digits
number = 1234
total = 0

while number > 0:
    digit = number % 10
    total = total + digit
    number = number // 10

print("Sum of digits:", total)  
# 4. Count digits in a number
number = 98765
count = 0

while number > 0:
    count = count + 1
    number = number // 10

print("Number of digits:", count)  
# 5. Factorial of a number
number = 5
factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print("Factorial:", factorial)  
# 6. Multiplication table
number = 7

for i in range(1, 11):
    print(number, "x", i, "=", number * i)
# 7. Check Armstrong number
number = 153
original = number
total = 0

while number > 0:
    digit = number % 10
    total = total + digit ** 3
    number = number // 10

if total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
# 8. Print even numbers from 1 to 20
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
# 9. Print odd numbers from 1 to 20
for i in range(1, 21):
    if i % 2 != 0:
        print(i)
# 10. Sum of numbers from 1 to 10
total = 0

for i in range(1, 11):
    total = total + i

print("Sum:", total) 