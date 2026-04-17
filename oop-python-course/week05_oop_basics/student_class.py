class Student:
    def __init__(self, name, student_id, course):
        self.name = name
        self.student_id = student_id
        self.course = course

    def display_student(self):
        print("Name:", self.name)
        print("Student ID:", self.student_id)
        print("Course:", self.course)

student1_lea = Student("Maria", "2023-001", "BSIS")
student1_lea.display_student()