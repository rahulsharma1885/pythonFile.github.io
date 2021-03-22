class Employee: 

	def __init__(self, name, salary, city): 
		self.name =name
		self.salary=salary
		self.city=city

	def detail(self): 
		print(f"the name is {self.name} and salary is {self.salary} and benongs to {self.city}") 


obj = Employee("Rahul", 50000, "meerut") 
obj.detail()
