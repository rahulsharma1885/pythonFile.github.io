class Person:
    company= "Yahoo"
    country="india"
    def display(self):
         print(self.company)
    
class Employee(Person):
    company="Google"
    def display(self):
        super().display()
        print(self.company)
    
class Programmer(Employee):
    company= "Honda"
    def display(self):
        super().display()
        print(self.company)

p=Person()
e= Employee()
pr=Programmer()
pr.display()