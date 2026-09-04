# REGULAR EXPRESSIONS IN PYTHON
import re
# re.search()
text = "I am learning Python"
result = re.search("Python", text)
if result:
    print("Word found")
else:
    print("Word not found")
#re.findall()
text = "My phone number is 9876543210 and pin code is 560001"
numbers = re.findall(r"\d+", text)
print(numbers)
#re.match()
text = "Python is easy"
result = re.match("Python", text)
if result:
    print("Text starts with Python")
# Match a single digit
text = "Room number is 25"
result = re.findall(r"\d", text)
print(result)
# Match a word character
text = "Hello123!"
result = re.findall(r"\w", text)
print(result)
#  Match spaces
text = "Python is fun"
result = re.findall(r"\s", text)
print(result)
# Match words starting with P
text = "Python Programming Practice"
result = re.findall(r"\bP\w*", text)
print(result)
# Mobile  number validation
mobile = "9876543210"
pattern = r"^[6-9]\d{9}$"
if re.match(pattern, mobile):
    print("Valid mobile number")
else:
    print("Invalid mobile number")
# Replace text using re.sub()
text = "My number is 98765"
new_text = re.sub(r"\d", "*", text)
print(new_text)
# Split text using re.split()
text = "Python,Java;C++ HTML"
languages = re.split(r"[,; ]+", text)
print(languages)