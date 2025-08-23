age = int(input("Enter your age: "))

if(age>18):
  print("You can drive.")
elif(age == 18):
  print("Let's schedule an interview.")   
elif(age == 0):
  print("Hey, you were just born.")    
else:
  print("Sorry! you cannot drive.")  