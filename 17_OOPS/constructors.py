class Employee:

  salary = 80000
  def __init__(self, salary, name, bond):
      self.salary = salary # create instance atrribute of name salary
      self.name = name # and assign it with salary
      self.bond = bond
  
  def get_salary(self):
      return self.salary
  
  def get_info(self):
     print(f"The name of the Employee is {self.name}. Salary is {self.salary}.The bond is for {self.bond} years")
  
e1 = Employee(80000, "Arshad", 4)
print(e1.get_salary())
e1.get_info()



 