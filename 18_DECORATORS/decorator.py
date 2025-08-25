# Decorator is a function that takes a function,
# it created a new function inside its body(wrapper).
# Then it returns that new function

def decorator(func):
       def wrapper():
             print("Hi!")
             print("I'm ARSHAD")
             func()
       return wrapper      


def say_hello():
    print("Hello!")

decorator(say_hello)()   




