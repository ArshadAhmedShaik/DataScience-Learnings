a = int(input("Enter number 1:"))
b = int(input("Enter number 2:"))


if b == 0:
  raise ValueError("Please don't divide by 0")

print(f"The sum is {a / b}")