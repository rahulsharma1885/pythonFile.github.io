class Programmer:
    def __init__(self, name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(f"my name is {self.name} and my salary is {self.salary}")    

rahul= Programmer("Rahul",50000)
rahul.display()
mohit= Programmer("Mohit",60000)
mohit.display()
