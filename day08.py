#sets
# duplicates are removed
numbers = {1, 2, 3, 4, 4}
print(numbers)  
# Add an item
numbers.add(5)
print(numbers)
# Remove an item
numbers.remove(2)
print(numbers)
# Check if an item exists
print(3 in numbers) 
# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # Union: {1, 2, 3, 4, 5}
print(a & b)  # Intersection: {3}
print(a - b)  # Difference: {1, 2}
#DICTIONARIES --------------------

student = {
    "name": "Anita",
    "age": 20,
    "course": "Python"
}

# Access values
print(student["name"]) 
print(student["age"])   
# Add and update values
student["age"] = 21
student["city"] = "Delhi"
print(student)
# Remove an item
del student["course"]
print(student)
# Check if a key exists
print("name" in student)  
# Loop through a dictionary
for key, value in student.items():
    print(key, ":", value)

# Dictionary example
marks = {
    "Anita": 85,
    "Rahul": 90,
    "Meera": 78
}

print(marks["Rahul"])  