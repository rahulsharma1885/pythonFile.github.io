class Mohit:
    def __init__(self, name, city, education):
        self.name=name
        self.city=city
        self.education=education
    def detail(self):
       print(f"My name is {self.name} and i am from {self.city} and i have done my {self.education}")
obj=Mohit("Mohit","meerut","B.tech")
obj.detail()