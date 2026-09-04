#contro statements
# 1. if statement
age = 18

if age >= 18:
    print("You are eligible to vote")
# 2. if-else statement
number = 7
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
# 3. if-elif-else statement
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# 4. Nested if statement
username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Wrong username")
# 5. for loop
for i in range(1, 6):
    print(i)

# 6. while loop
count = 1

while count <= 5:
    print(count)
    count += 1
# 7. break statement
for i in range(1, 10):
    if i == 5:
        break
    print(i)  
# 8. continue statement
for i in range(1, 6):
    if i == 3:
        continue
    print(i)  
# 9. pass statement
for i in range(1, 4):
    if i == 2:
        pass  
    print(i)