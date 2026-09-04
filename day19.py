# PYTHON FILE AND DIRECTORY OPERATIONS
import os
from pathlib import Path

#  FILE OPERATIONS
# 1. Create and write to a file
with open("notes.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("File handling example.\n")
# 2. Read the complete file
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
# 3. Read one line
with open("notes.txt", "r") as file:
    first_line = file.readline()
    print(first_line)
# 4. Read all lines
with open("notes.txt", "r") as file:
    lines = file.readlines()
    print(lines)
# 5. Append text to a file
with open("notes.txt", "a") as file:
    file.write("This line is added later.\n")
# 6. Check whether a file exists
if os.path.exists("notes.txt"):
    print("File exists")
# 7. Rename a file
os.rename("notes.txt", "python_notes.txt")
# 8. Delete a file
if os.path.exists("python_notes.txt"):
    os.remove("python_notes.txt")
#  DIRECTORY OPERATIONS
# 1. Get the current working directory
print(os.getcwd())
# 2. Create a directory
if not os.path.exists("my_folder"):
    os.mkdir("my_folder")
# 3. Create nested directories
os.makedirs("project/data", exist_ok=True)
# 4. List files and folders in the current directory
items = os.listdir(".")
print(items)
# 5. Check whether a path is a file or directory
path = "my_folder"
if os.path.isfile(path):
    print("It is a file")
elif os.path.isdir(path):
    print("It is a directory")
# 6. Change the current working directory
os.chdir("my_folder")
print(os.getcwd())
# Move back to the parent directory
os.chdir("..")
# 7. Remove an empty directory
if os.path.exists("my_folder"):
    os.rmdir("my_folder")