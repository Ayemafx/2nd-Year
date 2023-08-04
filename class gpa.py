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
    else:
        print("Student not found")


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


def bubble_sort(students):
    n = len(students)
    for i in range(n - 1):
        for j in range((n-i) - 1):
            if students[j].reg_no > students[j + 1].reg_no:
                students[j], students[j + 1] = students[j + 1], students[j]



students = []
students.append(Student(1, "Ayema Faisal", "BSSE", 3.5))
students.append(Student(2, "Abdul Rafay", "BSSE", 3.7))
students.append(Student(3, "Abdul Rafay Atiq", "BSSE", 3.0))
students.append(Student(7, "Aleezeh Rehman", "BSSE", 2.8))
students.append(Student(8, "Amna Noor Farooqi", "BSSE", 3.5))
students.append(Student(10, "Areeg Naeem", "BSSE", 3.2))


# call linear search to display data of student with a particular Regn no.
linear_search(students, 1)

# call bubble sort to arrange data of students according to Regn no.
bubble_sort(students)

# call binary search to display data of a student with a particular Regn no
binary_search(students, 10)