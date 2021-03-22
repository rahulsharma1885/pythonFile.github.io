class Employee:
    company="google"
    salary =22298
    def printDetails(self):
        print(f"the name is {self.name} and salary is {self.salary} and company is{self.compay}")
rahul= Employee()
rahul.name="rahul"
rahul.salary=1000
print(rahul.printDetails())
