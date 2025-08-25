class Employee:

  company = "Asus"

  def __init__(self, salary, name, bond, company):
      self.salary = salary # create instance atrribute of name salary
      self.name = name # and assign it with salary
      self.bond = bond
      self.company = company
  
  def get_salary(self):
      return self.salary
  
  def get_info(self):
     print(f"The name of the Employee is {self.name}. Salary is \
           {self.salary}.The bond is for {self.bond} years")
  
e1 = Employee(80000, "Arshad", 5, "Google")
print(Employee.company) # class attribute will be printed
print(e1.company) # instance attribute

#Object introspection:
print(dir(e1))
print(dir(Employee))



