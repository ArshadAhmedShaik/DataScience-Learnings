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

#for x in my_dict:
    # print(x)  this prints only keys :)

# for x in range(4, 50):
# #   print(x)

# numbers = [1, 2, 3 , 4]
# num_list = list(map(lambda x: x**2 ,numbers))
# print(num_list)

# OOPS:

# each object -> data(attributes) -> actions(methods)
# reusablity -> reusing same class multiple times
# OOPS -> to represent real world objects as code
# and establishing relationships btw them

# 4 pillars of OOPS:

'''
1) Abstraction: Hiding complex details and showing only the essential information to the users
2) Encapsulation: A class encapsulates: 1)attributes(data) + 2)Methods(actions), protects data
3) Inheritance: Inheriting attributes and methods of a parent class to a child class
4) Polymorphism: poly(many), morph(forms) || Animal class has a method -> Dog inherits the method with same name but diff operation
'''

# class(Blueprint) : it is like instructions for creating an object
# object(Instance) : instance created from the class/blueprint
# each object has its own set of unique data

# class -> architechtural plan
# object -> actual house built from that plan

# OOPS code:

# class Dog:
#   # this is a class attribute
#   species = "Canis familiaris"
#   # this is a constructor
#   def __init__(self, name, breed):
#     print(name, breed, sep = ",")
#     self.name = name #instance attribute
#     self.breed = breed #instance attribute
#   def bark(self):
#     print(f"{self.name} says Woof!")

# # create some Dog objects:

# my_dog = Dog("hehe", "GermanShepered")
# another_dog = Dog("bebe", "Golden Retriever")

# print(my_dog.name)
# print(my_dog.breed)
# print(another_dog.name)
# print(another_dog.breed)

# my_dog.bark()

# print(Dog.species)

# chat-gpt question:

# class Car:
#     # this is a class attribute
#     wheels = 4
#     # for instance attributes we need a constructor:
#     def __init__(self, brand, model):
#           self.brand = brand
#           self.model = model
#     def drive(self):
#           print(f"{self.brand} {self.model} is driving!")
  

# # Creating Car objects
# car1 = Car("Toyota", "Corolla")
# car2 = Car("Tesla", "Model S")

# # Accessing attributes
# print(car1.brand)     # Output: Toyota
# print(car2.model)     # Output: Model S
# print(Car.wheels)   
#   # Output: 4 (class attribute shared by all cars)

# # Calling methods
# car1.drive()          # Output: Toyota Corolla is driving!
# car2.drive()          # Output: Tesla Model S is driving!


# What is self?
# inside a class self means "this particular object"
# way of an object representing itself

# class vs instance attributes:

# class -> shared by all objects
# instance attributes ->usually defined within __init__ method
# specific to that particular object

# constructor:

# class Dog:
#   def __init__(self, name="Unknown", breed="Mixed"):
#     print("Welcome to the constructor!")
#     self.name = name
#     self.breed = breed

# my_dog = Dog()
# my_dog = Dog(breed="hehe")
# print(my_dog.name)
# print(my_dog.breed)
# my_dog = Dog("Fido", "Poodle")

# inheritance:

# class Dog(Animal):
#   def __init__(self, name):
#     self.name = name
# # Override from parent class 
# # specific to this object
#   def speak(self):
#     print("Woof!")

# class Cat(Animal):
#   def speak(self):
#     print("Meow!")

# my_dog = Dog("Rover")
# my_cat = Cat("Fluffy")

# print(my_dog.name)
# print(my_cat.name)

# my_dog.speak()
# my_cat.speak()


# what is super() ?

# class Animal:
#   def __init__(self, name):
#     self.name = name
#   def speak(self): # generic thing/ overall thing
#     print("Generic animal sound") 

# class Bird(Animal):
#    def __init__(self, name, wingspan):
#      super().__init__(name)
#      self.wingspan = wingspan     

# my_bird = Bird("Tweety", 10)
# print(my_bird.name)
# print(my_bird.wingspan)

# child can acces the parent's method by calling super().method()

# MAGIC-METHODS❤️ OR DUNDER-METHODS❤️:
# useful for operator overloading
# methods have double underscores at front and behind the method name

# class Point:
#   def __init__(self, x, y):
#     self.x = x
#     self.y = y
#   def __add__(self, other):
#     return Point(self.x + other.x, self.y + other.y)
#   # represents calss objects in the form of string roii  
#   def __str__ (self):
#     return f"({self.x}, {self.y})"
#   def __eq__(self, other):
#     return (self.x==other.x) and (self.y==other.y)
    
# p1 = Point(1, 2)
# p2 = Point(1, 2)

# p3 = p1 + p2

# # when you print(p3) it will call the dunder method -> __str__(self)....etc;
# print(p3)

# print(p1==p2)

# getters and setters(controlling access to attributes):
# Instead of exposing attributes directly,
# we provide getters (to read) and setters (to modify).
# getters and setters are for encapsulation in a class.

# dict = {x:x**2 for x in range(0,10)}

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self._age = age

#   def get_age(self):
#     return self._age  
    
#   def set_age(self, new_age):
#     if new_age >= 0 and new_age <= 150:
#       self._age = new_age
#     else:
#       print("Invalid age!")    

# person = Person("Alice", 30)
# # print(person.get_age())

# # person.set_age(35)
# # print(person.get_age())

# # person.set_age(-10)
# # print(person.get_age())

# # The pythonic way: @property decorator

# # class Person:
# #     def __init__(self, name, age):
# #       self.name = name
# #       self._age = age
# #     @property  #getter
# #     def age(self):
# #        return self._age
# #     @age.setter
# #     def age(self, new_age):
# #         if(new_age >= 0 and new_age <= 150):
# #           self._age = new_age
# #         else:
# #            print("Invalid age")

# # # @property and @age.setter

# # person = Person("Bob", 40)
# # print(person.age)
# # person.age = 47
# # print(person.age)
# # person.age = -22
# # print(person.age)

# #  @property -> name can be age 
# #  @age.setter -> same name used in property
       
# # (_age) -> convention for private use 
# # in class only! don't access this
# #  directly from outside the class; 
# # use the provided getters and setters 
# # instead        

# class MyClass:
#    def __init__(self):
#       self._internal_value = 0

#    @property
#    def internal_value(self):
#       return self._internal_value
   
#    @internal_value.setter
#    def internal_value(self, value):
#       self._internal_value = value

#    # wrong x infinite recursion! bro!
# #    def _internal_value(self):
# #       return self._internal_value   

# obj = MyClass()

# print(obj.internal_value)
# obj.internal_value = 45
# print(obj.internal_value)

# decorators: meta-programming
# where one part of the program tries to modify 
# another part of the program at compile time

# can accept functions and return functions as well!

# def my_decorator(func):
#     def wrapper():
#        print("Before calling func()")
#        func()
#        print("After calling func()")
#     return wrapper   


# # the wrapper function adds 
# # behaviour before 
# # and after the function call

# @my_decorator
# def say_hello():
# #   print("Hello")

# # f = my_decorator(say_hello)
# # f()

# # using decorators with arguments:


# def repeat(n):
#   def decorator(func):
#     def wrapper(name):
#       for i in range(n):
#         func(name)
#     return wrapper
#   return decorator    



# @repeat(3)
# def greet(name):
#   print(f"Hello, {name}!")


# greet("Arshad")


# def uppercase(func):
#   def wrapper(name):
#       result = func(name)
#       return result.upper()
#   return wrapper    

# @uppercase
# def say(name):
#   return f"Hello, {name}"

# print(say("Arshad"))

# chaining multiple decorators
# bottom to top:

# def uppercase(func):
#   def wrapper():
#     return func().upper()
#   return wrapper

# def exclaim(func):
#   def wrapper():
#     return func() + "!!!"
#   return wrapper
 
# @uppercase  # this will be shown as output
# @exclaim
# def greet():
#   return "hello"

# print(greet())

# order -> bottom to top

# the function will be decorated from
# bottom to up
# finally top one is shown in output

# getters and setters in python

# provide a way to encapsulate
# _ before variable is used as a 
# # convention for private var in py

# # traditional approach:

# class Person:
#   def __init__(self, name):
#     self._name = name
#   def get_name(self):
#     return self._name
#   def set_name(self, new_name):
#     self._name = new_name

# p = Person("Arshad")
# print(p.get_name())
# p.set_name("bru")
# print(p.get_name())

# # python way of doing it:

# # @property -> getter
# # @var.setter -> setter

# class Person:
#   def __init__(self, name):
#     self._name = name
#   @property
#   def name(self):
#     return self._name 
#   @name.setter
#   def name(self, new_name):
#     self._name = new_name

# p = Person("Arshad")
# print(p.name)
# p.name = "Brindha"
# print(p.name)


# if u want read only properties then just omit
# @var.setter

# @property.deleter -> it deletes a property

# class Person:
#   def __init__(self, name):
#     self._name = name
#   @property
#   def name(self):
#     return self._name
#   @name.setter
#   def name(self, new_name):
#     self._name = new_name
#   @name.deleter
#   def name(self):
#     del self._name    

# p = Person("Arshad")
# print(p.name)
# del p.name
# print(p.name) -> produces error
# as the attribute is deleted

# read only property:
# include only @property
# but not @var.setter

# static,class,instance methods in python:

'''
1) instance methods
2) class methods
3) static methods -> no self or cls
'''

# 1) instance(default in py)

# class Dog:
#   def __init__(self, name):
#     self._name = name
#   def speak(self):
#     return f"{self._name} barks"

# dog = Dog("Yaga")
# print(dog.speak())  
# 
# 
# # class methods:
# # 
# class Animal:
#   species = "Mammal"  #this is a class attribute
#   @classmethod
#   def set_species(cls, new_species):
#     cls.species = new_species
#   @classmethod
#   def get_species(cls):
#     return cls.species


# # # print(Animal.get_species())
# # # Animal.set_species("Reptile")
# # # print(Animal.get_species())

# # # you can also call class methods on instances

# # a = Animal()
# # print(a.get_species())

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   @classmethod
#   def from_string(cls, data):
#     name, age = data.split("-")
#     return cls(name, int(age))  

# p = Person.from_string("Arshad-70")
# print(p.name, p.age)

# static method:
# they don't take self or cls as parameters

# class MathUtils:
#   @staticmethod
#   def add(a, b):
#     return a + b
  
# print(MathUtils.add(3, 5))

# dunder methods:

# # 1) __init__

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p = Person("Arshad", 45)
# print(p.name, p.age) 

# __str__ and __repr__

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   def __str__(self):
#     return f"Person({self.name}, {self.age})"  
#   def __repr__(self):
#     return f"Person(name = '{self.name}', age = {self.age})"

# p = Person("Arshad", 30)
# print(str(p))
# print(repr(p))
# print(p)

# 3) __len__()

# class Book:
#   def __init__(self, title, pages):
#     self.title = title
#     self.pages = pages
#   def __len__(self):
#     return self.pages 

# b = Book("Python 101", 250)
# print(len(b))
# 
# # 4) operator overloading add,sub,mul

# exceptional handling and custom errors in python

# errors in python:

# while True:
#   try:
#     a = int(input("Enter number 1:"))
#     b = int(input("Enter number 2:"))
#     print(f"The sum is {a + b}")
#   except ValueError:
#     print("Please don't perform bad calculations")  
#   except ZeroDivisionError:
#     print("Hey! don't divide by 0")  
#   except Exception as e:
#     print("Some error occured", e)  



a = int(input("Enter number 1:"))
b = int(input("Enter number 2:"))


if b == 0:
  raise ValueError("Please don't divide by 0")

print(f"The sum is {a / b}")















































