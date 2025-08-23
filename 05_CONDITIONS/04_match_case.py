a = int(input("Enter a number btw 1 and 10:"))

match a:
   case 1:
      print("you won a charger")
   case 3:
      print("you won $3")   
   case 6:
      print("The won a camera")   
   case _:
      print("Better Luck next time")
   