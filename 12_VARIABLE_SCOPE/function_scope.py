# def sum(a, b):
#   c = a + b
#   return c
# z = 8
# def sum(a, b):
#   z = a + b
#   return z
# print(z)
# print(sum(1,2))

def greet():
  global z
  z = 32 # local variable
  print("Hello")

greet()
print(z)

