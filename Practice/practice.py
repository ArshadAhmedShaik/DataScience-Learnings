# # text = "Python"
# # print(f"{text:>10}") #right align
# # print(f"{text:<10}") #left align
# # print(f"{text:^10}") #center align


# # lambda functions in py

# # normal function:

# def add(a, b):
#   return a + b

# # lambda function:

# add_lambda = lambda x, y: x + y

# # takes in x,y and returns x+y

# print(add(2,3))
# print(add_lambda(2,3))

# # square of a number
# square = lambda x: x*x
# print(square(3))

# # lambda is an anonymous function:
# numbers = [1, 2, 3, 4]
# squared = list(map(lambda x: x**2, numbers))
# print(squared)

# # question to master lambda fucntion using map and list:

# numbers = [5, -3, 8, -1, -1, 7]
# new_list = list(map(lambda x: abs(x), numbers))
# print(new_list)
# a = tuple(new_list)
# print(a)
# # b = set(new_list)
# # print(b)

# # recursion in python:

# # def factorial(n):
# #   if n == 1 or n == 0:
# #     return n
# #   return n*factorial(n-1)

# # print(factorial(5))

# # Modules:

# import math
# print(math.sqrt(16))

# import my_module
# my_module.print_arshad()


# # u can also use external
# #  libraries by installing them
# #  using pip installer


# function scope and lifetime

# in py var -> scope and lifetime
# var exist till function returns after that
# they get destroyed

# x = 10

# def my_func():
#   x = 5
#   print(x)

# my_func()
# # print(x)

# # what is global key word?

# x = 10

# def modify_global():
#   global x
#   x = 5

# modify_global()
# print(x)  

# docstrings: - func documentation

# def add(x, y):
#   '''Returns the sum of two numbers.'''
#   return x + y

# print(add.__doc__)

# proper way of writing them is:

# # def add(a, b):
#     '''
#     Returns the sum of two numbers

# #     Parameters:
# #     a (int): the first number
# #     b (int): the second number

# #     Returns:
# #     int: The sum of two numbers.
# #     '''

# #     return a + b

# # # print(add.__doc__)

# names = ["alice", "BOB", "ChArLiE", "david", "Eve"]

# new_names = list(map(lambda x: x.lower(), names))
# print(new_names)
# new_names = list(map(lambda x: x.upper(), names))
# print(new_names)
# new_names = list(map(lambda x: x.capitalize(), names))
# print(new_names)

# bonus question:

# nums = [10, 25, 30, 45, 60]

# nums = list(map(lambda x: f"{x} USD",nums))
# print(nums)

# a = "Hello, Python"
# b = 'Hello, Python'
# c = '''
#             hi bros
#             what's up ...
           
#  hehe            
# '''


# print(a)
# print(b)
# print(c)

# text = "Python"

# print(text[0])
# print(text[1])
# print(text[-1]) #last character

# string slicing: (like substring in java)
# text = "Hello, Python!"
# print(text[0:5])
# print(text[:5])
# print(text[7:]) # left - include , right - exclude
# print(text[::2]) # 0,2,4 ETC...
# String methods:
# text = "hello world"
# print(text.upper())

# text = "hellO sorld  "
# # print(text.lower())
# # print(text.strip())
# # print(text.lstrip())
# # print(text.rstrip())
# # print(text.replace("hel", "Arshad"))
# # print(text.strip().split('$'))
# print(text.title())\


# string formatting:

# name = input("Ënter name:")
# age = int(input("Enter age:"))

# # using format(variables)

# # print("My name is {} and I am {} years old.".format(name, age))

# string = "My name is {} and I am {} years old.".format(name, age)
# print(string)


#f-strings:

# name = "Arshad"
# age = 20

# print(f"My name is {name} and I am {age} years old!")

# multi-line strings:

# message = '''

#         Hello,
#         This is a multi-line string example
#         GoodBye!

# '''

# print(message)


# text = "Welcome to Python!"

# print(text[3:-3])
# print(text[-1:-5:-1])

# # reverse a string:

# text = "Arshad"

# print(text[::-1])

# text = " hello woRld "
# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.capitalize())

#removing white-space:

# print(text.lstrip())
# print(text.rstrip())
# print(text.strip())

# text = "PyFhon is Fun"

# print(text.find("F"))
# print(text.replace("F", "Arshad"))

# splitting and joining:

# text = "apple,banana,orange"
# fruits = text.split(',')
# print(fruits[-1])
# fruits[0] = fruits[1]
# print(fruits)

# text = ",".join(fruits)
# print(type(text))
# print(text)

# # checking string properties:

# text = "\t   \n"
# print(text.isdigit())
# print(text.isalpha())
# print(text.isalnum())
# print(text.isspace()) #checks if all characters
# #in string whitespace characters

# isalnum()

# Built in string functions:

# text = "Hello, Python!"
# print(len(text))

# # for finding ascii values:

# print(ord('a'))
# print(chr(97))
# print(chr(65))

# ord, chr

# name = "Arshad"
# age = 30

# print("My name is {name} and age is {age}".format(name = "Bindu", age = 25))

# x = 10
# y = 20

# # print(f"The sum of {x} and {y} is {x+y}")

# # formatting numbers:

# pi = 3.1475685685
# num = float(f"{pi:.2f}")
# print(num+1)


# # allignment of text:
# text = "Python"



# also used for padding:

# print(f"{text:<10}")
# print(f"{text:^100}")

# # these are for allignment

# text = r"\n"
# text1 = R"\\\""

# print(text)
# print(text1)

# # "".join(list) better than iterating and joining characters

# functions and modules:

# functions and modules:

# function to greet someone:

# def greet(name):
#     print(f"Hello, {name}!")
   
# greet("Arshad")

# types of arguments;

# 1) Positional arguments:

# def add(a, b):
#     return a+b
       
# print(add(10,5))    

# # 2) default arguments:

# def greet(name = "Guest"):
#     return f"Hello, {name}!"
   
# print(greet())    

# 3) keyword arguments:

# def student(name, age):
#     print(f"Name: {name}, Age: {age}")

# student(age = 20, name = "Arshad".lower())

# Data Structures in python:

# 1) List and its methods
# mutable:
# numbers = [1,2,3,4]
# numbers = [1,"love","hate"]

# for x in numbers:
#   print(x, end = ",")

# my_list = [1,2,3]

# # my_list.append((1,45))

# # print(type(my_list[-1]))

# # print(my_list)

# my_list.insert(2, 7)
# print(my_list)

# my_list[-1] = 56
# print(my_list)

# my_list.extend([1,2,3])
# print(my_list)

# my_list.pop(-1)
# print(my_list)

# my_list.reverse()
# print(my_list)

# my_list.sort()
# print(my_list)

# list comprehensions:

# squared = [x**2 for x in range(0, 5)]
# print(squared)

# squared = [x*3 for x in range(0, 6)]
# print(squared)

# 2) Tuples:

# my_tuple = (10, 20, 30, 10)
# # single_element = (1, )

# # print(single_element)
# # print(my_tuple[-1])

# # tuple unpacking

# a,b,c,d = my_tuple
# print(a)
# print(b)
# print(c)

# # tuple methods common:

# print(my_tuple.count(-1))
# print(my_tuple.index(20))

# why use tuples?

# -> faster than lists (immutable)
# -> dictionary keys 

# each value of a dictionary.items() is a tuple

# 3) Sets:

# fruits = {"apples", "banana", "cherry"}

# sets = {1,2,3,4}
# sets.add(5)
# sets.remove(2)
# sets.discard(-1)
# print(sets)

# set operations:

# a = {1, 2, 3}
# b = {3, 4, 5}

# print(a.union(b))
# print(a.difference(b))
# print(a.intersection(b))

# use case: sets are great for 
# eliminating values

# 4) dictionary methods:

# student = {"name": "Alice", "age": 21, "grade": "A"}

# print(student["name"])
# student["age"] = 45

# student["city"] = "NewYork"

# print(student)

# list1 = student.items()
# list2 = student.values()
# list3 = student.keys()

# print(list1)
# print(list2)
# print(type(list(list3)))

# print(type(list3))

# student.pop("name")

# print(student)

# # dictionary comprehensions:

# squares = {x:x**2 for x in range(0, 5)}
# print(squares)























