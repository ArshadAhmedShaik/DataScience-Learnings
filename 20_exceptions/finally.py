a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

try:
   c = a/b
except Exception as e:
   print(e) 
   # anything under finally is always executed no matter what 
finally:
    print("This is always executed!")     