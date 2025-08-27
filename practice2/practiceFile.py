# map, filter, reduce:
# def func(a, b):
#     return a**2 + b**2

# numbers = [1, 2, 3, 4, 5]
# num = list(map(func, numbers))
# print(num)

# numbers1 = [1, 2, 3]
# numbers2 = [4, 5, 6]

# summed = map(lambda x, y: x + y, numbers1, numbers2)

# print(list(summed))

# list comprehensions:

# numbers = [1, 2, 3, 4]
# squared_numbers = [x**2 for x in numbers]
# print(squared_numbers)

# filter() function:

# numbers = [1, 2, 3, 4, 5]
# even_numbers = filter(lambda x: x % 2 == 0, numbers)
# print(list(even_numbers))

# # equivalent list comprehension:

# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers_lc = [x for x in numbers if x % 2 == 0]
# print(even_numbers_lc)

# # Example with None as function

# values = [0, 1, [], "hello", "", None, True, False]
# truthly_values = filter(None, values)
# print(list(truthly_values))
# # reduce function:


# from functools import reduce

# numbers = [1, 2, 3, 4, 5, 6]

# sum_of_numbers = reduce(lambda x, y: x+y, numbers)
# print(sum_of_numbers)

# reduce with initializer:
# here 7 is an initializer
# empty_list_sum = reduce(lambda x,y: x+y, [1, 2, 3], 7)
# print(empty_list_sum)


# total = 0
# for x in numbers:
#   total += x
# print(total)  

# walrus operator: (it is an assignment operator)

# data = input("Enter a value (or 'quit' to exit): ")

# while data!="quit":
#   print(f"You entered: {data}")
#   data = input("Enter a value (or 'quit' to exit): ")

# while (data:=input("Enter a value (or 'quit' to exit): ")):
#       print(f"You entered: {data}")
#       if(data=='quit'): break
      
# walrus operator is used in list operations:

# numbers = [1, 2, 3, 4, 5]

# #without walrus operator:
# results = [x*2 for x in numbers if x*2>5]
# print(results)

# #with walrus operators:
# results = [y for x in numbers if (y:= x*2)>5]
# print(results)

# it's easy to read files using walrus operator:

# with open("arshad.txt", "r") as f:
#       line = f.readline()
#       while line:
#             print(line.strip())
#             line = f.readline()

# with open("arshad.txt", 'r') as f:
#       while(line:=f.readline()):
#             print(line.strip())

