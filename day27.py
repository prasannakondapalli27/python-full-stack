# UNIVERSITY MANAGEMENT SYSTEM - OOP PROJECT
class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Email:", self.email)
class Student(Person):
    def __init__(self, student_id, name, age, email, course):
        super().__init__(name, age, email)
        self.student_id = student_id
        self.course = course
        self.marks = {}
    def add_mark(self, subject, mark):
        self.marks[subject] = mark
    def show_marks(self):
        print("Marks for", self.name)
        for subject, mark in self.marks.items():
            print(subject, ":", mark)
    def calculate_average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks.values()) / len(self.marks)
    def show_student(self):
        print("\nStudent ID:", self.student_id)
        self.show_details()
        print("Course:", self.course)
        self.show_marks()
        print("Average:", self.calculate_average())
class Professor(Person):
    def __init__(self, professor_id, name, age, email, department):
        super().__init__(name, age, email)
        self.professor_id = professor_id
        self.department = department
        self.subjects = []
    def add_subject(self, subject):
        self.subjects.append(subject)
    def show_professor(self):
        print("\nProfessor ID:", self.professor_id)
        self.show_details()
        print("Department:", self.department)
        print("Subjects:", ", ".join(self.subjects))
class Course:
    def __init__(self, course_code, course_name, professor):
        self.course_code = course_code
        self.course_name = course_name
        self.professor = professor
        self.students = []
    def enroll_student(self, student):
        self.students.append(student)
    def show_course(self):
        print("\nCourse Code:", self.course_code)
        print("Course Name:", self.course_name)
        print("Professor:", self.professor.name)
        print("Enrolled Students:")
        for student in self.students:
            print("-", student.name)
class University:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.professors = []
        self.courses = []
    def add_student(self, student):
        self.students.append(student)
    def add_professor(self, professor):
        self.professors.append(professor)
    def add_course(self, course):
        self.courses.append(course)
    def show_university_details(self):
        print("\nUniversity:", self.name)
        print("Total Students:", len(self.students))
        print("Total Professors:", len(self.professors))
        print("Total Courses:", len(self.courses))
# Create university
university = University("ABC University")
# Create professor
professor1 = Professor(
    "P101",
    "Dr. Sharma",
    45,
    "sharma@university.com",
    "Computer Science"
)
professor1.add_subject("Python")
professor1.add_subject("Data Structures")
# Create students
student1 = Student(
    "S101",
    "Anita",
    20,
    "anita@email.com",
    "BCA"
)
student1.add_mark("Python", 85)
student1.add_mark("Data Structures", 90)
student2 = Student(
    "S102",
    "Rahul",
    21,
    "rahul@email.com",
    "BCA"
)
student2.add_mark("Python", 78)
student2.add_mark("Data Structures", 82)
# Create course
course1 = Course("CS101", "Python Programming", professor1)
# Enroll students in course
course1.enroll_student(student1)
course1.enroll_student(student2)
# Add data to university
university.add_professor(professor1)
university.add_student(student1)
university.add_student(student2)
university.add_course(course1)
# Display details
university.show_university_details()
professor1.show_professor()
student1.show_student()
student2.show_student()
course1.show_course()