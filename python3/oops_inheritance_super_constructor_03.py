class Person:
    def __init__(self):
        print("initalizing Person \n")
    def display(self):
        print("im rahul 1")

class Employee(Person):
    def __init__(self):
        super().__init__()
        print("initalizing Employee \n")
  
    def display(self):
        super().display()
        print("im rahul 2")
class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("initalizing Programmer \n")
  
    def display(self):
        super().display()
        print("im rahul 3")
p= Person()
e= Employee()
pr= Programmer()
