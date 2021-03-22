class Employee:
    company= "Google"
    def display(self):
        print(f"this is an Employee and company is: {self.company}")
class Programmer(Employee):
    def display1(self):
        print(f"this is a programmer {self.company}, and my name is {self.name} ")

rahul= Employee()
rahul.display()

mohit= Programmer()
mohit.name="Mohit Sharma"
mohit.display1()
