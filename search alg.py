class Student:
    def __init__(self, reg_no, name, course, cgpa):
        self.reg_no = reg_no
        self.name = name
        self.course = course
        self.cgpa = cgpa

    def display(self):
        print("Regn No.: ", self.reg_no)
        print("Name: ", self.name)
        print("Course: ", self.course)
        print("CGPA: ", self.cgpa)

def linear_search(students, reg_no):
    for student in students:
        if student.reg_no == reg_no:
            student.display()
            return
    print("Student not found")

def bubble_sort(students):
    n = len(students)
    for i in range(n-1):
        for j in range(n-i-1):
            if students[j].reg_no > students[j+1].reg_no:
                students[j], students[j+1] = students[j+1], students[j]

def binary_search(students, reg_no):
    left = 0
    right = len(students) - 1
    while left <= right:
        mid = (left + right) // 2
        if students[mid].reg_no == reg_no:
            students[mid].display()
            return
        elif students[mid].reg_no < reg_no:
            left = mid + 1
        else:
            right = mid - 1
    print("Student not found")

# create a list of 50 students
students = []
students.append(Student(1001, "John", "Engineering", 8.5))
students.append(Student(1002, "Alice", "Arts", 9.0))
students.append(Student(1003, "Bob", "Science", 7.5))
# add more students here

# call linear search to display data of student with a particular Regn no.
linear_search(students, 1002)

# call bubble sort to arrange data of students according to Regn no.
bubble_sort(students)

# call binary search to display data of a student with a particular Regn no
binary_search(students, 1003)
