class Employee:
    company="google"
    salary="50000"
    city= "meerut"
class Programmer(Employee):
    name="Rahul Sharma"
    def getInfo(self):
        print(f"my name is {self.name} and my salary is {self.salary} and i live in {self.city}.")
rahul= Employee()
harry= Programmer()
harry.getInfo()