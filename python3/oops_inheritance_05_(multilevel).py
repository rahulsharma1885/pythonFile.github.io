class Person:
    company="google"
    country="india"
    def takeBreath(self):
        print("i am breathing")
    def display(self):
        print(self.company)
class Employee(Person):
    company="Honda"
    def getSalary(self):
        print(f"{self.salary}")
    def takeBreath(self):
        print("i am employee, i am luckelly breathing")
    def display(self):
        print(self.company)

class Programmer(Employee):
    def getSalary(self):
        print(f"{self.salary}")
    def takeBreath(self):
        print("i am employee, i am luckelly breathing++++")

p=Person()
e=Employee()
pr=Programmer()
pr.takeBreath()
pr.display()