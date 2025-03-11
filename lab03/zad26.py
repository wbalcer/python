class Student:
    def __init__(self):
        self.students = {}
    
    def add_student(self, name):
        self.students[name] = []
    
    def add_grade(self, name, grade):
        self.students[name].append(grade)
    
    def get_grades(self, name):
        return self.students.get(name, "Student nie istnieje.")
    
    def __str__(self):
        return str(self.students)

students = Student()
students.add_student("Jan")
students.add_grade("Jan", 5)
students.add_grade("Jan", 4)
students.add_student("Anna")
students.add_grade("Anna", 3)
print(students.get_grades("Jan"))
