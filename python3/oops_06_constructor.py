class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
        def details(self):
            print(f"{self.name} and {self.salary}")
rahul = Employee("rahul", 50000)
print(rahul.details())
