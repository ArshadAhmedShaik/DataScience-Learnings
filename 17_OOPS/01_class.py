# Class: Class is a blueprint. Eg. Form for an
#  Exam that contians name, age, ,lectives,father's name

# Object : Object is an instance of a Class(template)
# EG: Form that contains data of john

class Employee:
    company = "HP"
    def get_salary(self): # self is imp here cuz self is the way to refernce the object of 
        # class being created
        print(self)
        return 34000
        
    
e1 = Employee() #An object of class Employee is created here
print(e1.get_salary()) # Employee's get salary method is called her

e2 = Employee()
print(e2.get_salary())
print(e2.company)

