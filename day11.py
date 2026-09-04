# PYTHON PATTERN PROGRAMS
# 1. Square star pattern
for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()
# 2. Right triangle star pattern
for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()
# 3. Inverted right triangle
for i in range(4, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
# 4. Number triangle
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print(i)
# 5. Same number triangle
for i in range(1, 5):
    for j in range(i):
        print(i, end=" ")
    print()
# 6. Pyramid star pattern
for i in range(1, 5):
    print(" " * (4 - i), end="")
    print("* " * (2 * i - 1))
# 7. Inverted pyramid pattern
for i in range(4, 0, -1):
    print(" " * (4 - i), end="")
    print("* " * (2 * i - 1))
# 8. Floyd's triangle
number = 1

for i in range(1, 5):
    for j in range(i):
        print(number, end=" ")
        number += 1
    print()
# 9. Alphabet triangle
for i in range(1, 5):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()