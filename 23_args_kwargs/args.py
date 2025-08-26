from functools import reduce

def sum(*args):  #tuple form
  return reduce(lambda x, y: x + y, args) 

print(sum(342, 2, 7, 9))

