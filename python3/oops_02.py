class Employee:
    company= "google"
    salary = 3000

harry = Employee()
harry.name= "Harry"
harry.salary=2000

marry = Employee()
marry.name="Marry"
marry.company="youtube"

print(f"name is {marry.name} and company {marry.company} and salary is: Rs{marry.salary}" )
print(harry.name , harry.company, harry.salary)
