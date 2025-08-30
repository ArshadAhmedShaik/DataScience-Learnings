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

# without walrus operator:

# with open("arshad.txt", "r") as f:
#   line = f.readline()
#   while line:
#     print(line.strip())
#     line = f.readline()

# with walrus operator:

# with open("arshad.txt", "r") as f:
#   while(line:=f.readline()):
# #     print(line.strip())    

# with open("arshad.txt", "r") as f:
#   while(line:=f.readline()):
#     print(line.strip())

# why with?
# it automatically close the file
# no need to close it manually!

# Args and kwargs:
# *args, **kwargs

# *args -> positional variables -> stores in a tuple
# collects any extra positional variables
# *kwargs -> keyword arguments

#tuples:

# def my_function(*args):
#   print(type(args))
#   print(args)

# my_function(1)

# **kwargs:

# def my_function(**kwargs):
#   print(type(kwargs))
#   print(list(kwargs.keys()))

# my_function(name="Arshad", age=30)

# when using args and kwargs at the same time 
# use *args before **kwargs

# def my_function(a, b, *args, c = 10, **kwargs):
#   print(a)
#   print(b)
#   print(args)
#   print(c)
#   print(kwargs)

# my_function(1,2)  

# use of *args and **kwargs:
# can be used in decorators:

# example:

# class Animal:
#   def __init__(self, name):
#     self.name = name

# class Dog:
#   def __init__(self, name, breed, *args, **kwargs):
#     super().__init__(name)
#     self.breed = breed
#     print(args)
#     print(kwargs)

# dog1 = Dog("Buddy", "Golden Retriever")    
# dog2 = Dog("Licy", 1, 2, 3, color = "bLck", age = 5)
# 1,2,3 will be stored as (1,2,3) 
# in a tuple by args, and rest will
#  be stored as a map by **kwargs
# map = {1:23, "hello":45}
# print(list(map)) # converts t0 key list not value list

# reading from a file:

# try:
#   file = open("arshad.txt", "r")
#   content = file.read()
#   print(content)
#   file.close()
# except FileNotFoundError:
#   print("File Not Found")

# reading a file line by line:

# try:
#   file = open("arshad.txt", "r")
#   for line in file:
#     print(line.strip())
#   file.close()
# except FileNotFoundError:
#   print("File Not Found!")    

# writing to a file:
# with open("Arshad.txt", "w") as f:
#   f.write("Hello World!\n")
#   f.write("This is new Line!\n")
#   f.close()

# file = open("arshad.txt", "a")
# file.write("This is an appended text!\n")
# file.close()

# OS and shutil modules in python

# os -> deals with file,directories
# shutil -> offers higher level file operations!

import os

# current_dir = os.getcwd()
# print(current_dir)

# os.mkdir("new_directory")
# os.mkdir("24_FILES/new_directory")
# creates nested directorys

# os.chdir("new_directory")

# files = os.listdir(".")
# print(files)

#this removes only files!
# os.remove("my_file.txt")
# os.rmdir() -> removes empty directory!

# shutil.rmtree() removes non-empty directory
# os.rename("old.txt", "new.txt")

# if(os.path.exists("arshad.txt")):
#   print("File Exists!")
# print(os.path.exists("24_FILES/append.py"))

# path = os.path.join("folder", "")# u can always join path components!

# import shutil

# # shutil.rmtree()
# shutil.copy(".txt", ".txt")
# # copy from left to right

# shutil.move("arshad.txt", "....directory with /")
# what are command line utilities?
# handling command line arguments using argparse module
# from functools import reduce

import base64

import base64

encoded = "WW91IGFycml2ZSBhdCB0aGUgZ2F0ZXMgb2YgdGhlIEN1cmlvdXMgVmF1bHQuIFRoZSBhaXIgaXMgdGhpY2sgd2l0aCBteXN0ZXJ5LCBhbmQgYSBzdG9uZSB0YWJsZXQgYmVhcnMgYW4gaW5zY3JpcHRpb246ICJPbmx5IHRob3NlIGtub3duIGFzICdDdXJpb3VzX0V4cGxvcmVyJyBtYXkgc3RlcCBmb3J3YXJkLiBCZXlvbmQgdGhpcyBkb29yLCBzaGFkb3dzIGNvbmNlYWwgYSBzZWNyZXQuIFNlZWsgdGhlIGhpZGRlbiB0ZXh0IHdpdGhpbiAnL2ZpbmQta2V5Jy4gQnV0IGJld2FyZeKAlG9ubHkgdGhvc2UgcmVjb2duaXplZCBieSB0aGUgZ3VhcmRpYW5zIG9mICd3ZWJtaW5peC5jb20nIHdpbGwgYmUgYWxsb3dlZCBwYXNzYWdlLiI="
decoded = base64.b64decode(encoded).decode('utf-8')
print(decoded)


