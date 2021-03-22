class Person:
    def display(self):
        print("this is my page1")
class Employee(Person):
    def display(self):
        super().display()
        print("this is my page2")
class Programmer(Employee):
    def display(self):
        super().display()
        print("this is my page3")
p= Person()
e= Employee()
pr= Programmer()
pr.display()