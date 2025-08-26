import argparse

# step-1) write the description of the parser:
parser = argparse.ArgumentParser(description = "Working Calculator")
# step-2) Add arguments to parse

parser.add_argument("num1", type = float, help = "First Number")
parser.add_argument("num2", type = float, help = "Second Number")
parser.add_argument("operation", choices = ["add", "sub", "mul", "div"], help = "Operation to perform")

# step-3) U have to parse the arguments:
args = parser.parse_args()

# now u can access the arguments:
if(args.operation == "add"):
  print(f"{args.num1 + args.num2}")
elif(args.operation == "sub"):
  print(f"{args.num1 - args.num2}")
elif(args.operation == "mul"):
  print(f"{args.num1 * args.num2}")    
elif(args.operation == "div"):
  try:
    print(f"{args.num1/args.num2}")
  except Exception as e:
    print("Invalid division did re uuuuu")
    print(e)
  else:
    print("Hello") 
  # this one prints for both exception and non-exception cases combined   
  finally:
    print("Bye bro!!")  
else:
  print("Invalid arguments")    
  