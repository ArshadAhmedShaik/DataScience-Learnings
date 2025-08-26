numbers = [1, 2, 3, 45, 67, 9]
# map(function_name, iterable)
squared_numbers = list(map(lambda x:x*x,numbers))
print(squared_numbers)


# example:

def square(x):
  return x**2

lists = [1,2,3,4,5]
# returns a map object
new = list(map(square, lists))
print(new)

def fun(x):
  if(x>9):
    return True
  else:
    return False
  
a = [100,1,2,3,4,90]
new = list(filter(fun, a))
print(new)

# map, filter, reduce

