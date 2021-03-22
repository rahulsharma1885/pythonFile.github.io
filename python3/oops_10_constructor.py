
class Student:
    def __init__(self, name, college, rollno):
        self.name= name
        self.college= college
        self.rollno= rollno
    def detail(self):
        print(f"The student namer is {self.name} and the college {self.college} and the student roll number {self.rollno}")
stu = Student("Rahul Sharma", "JP", 59)
stu.detail()

