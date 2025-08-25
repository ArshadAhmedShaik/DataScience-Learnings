class Employee:
  company = "HP"

  def __init__(self, name, salary):
    self.name = name
    self.salary = salary

  #Instance method  
  def print_info(self):
     print(f"The name is {self.name} and the salary is {self.salary}" )

  @staticmethod
  def sum(a, b):
      return a + b

  @classmethod
  def print_company(cls):
     print(cls.company) 

  @classmethod
  def change_company(cls, c2):
     cls.company = c2   

e1 = Employee("Jack", 3000)
e2 = Employee("Jill", 4000)
print(Employee.company)  
# print(Employee.name)  
e1.print_info()

print(e2.sum(5, 23))
e1.print_company()

e1.change_company("Acer")
e1.print_company()
e2.print_company()
print(Employee.company)

