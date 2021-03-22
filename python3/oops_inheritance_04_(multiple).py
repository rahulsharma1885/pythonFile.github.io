class Employee:
    company="Google"
    id= 34545
class Programmer:
    company= "HCL"
class Person(Employee, Programmer):
    name= "rahul"
    def display(self):
      print(f"ny name is {self.name} and mu company {self.company}")
p= Person()
p.display()
