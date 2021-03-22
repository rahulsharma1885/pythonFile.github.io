class Employee:
    company="google"
    def getSalary(self):
        print(f"the name is {self.name} and the salary is:{self.salary} and company name is {self.company} ")
rahul= Employee()
rahul.name="Rahul"
rahul.salary=5000
print(rahul.getSalary())