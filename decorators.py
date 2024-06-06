import functools

#functions

def print_hello(message: str):
    print(message)

print_hello("hello")


#first class objects
#means function can be passed as an argument like any other datatype


def first_function(message: str):
    return message

def second_function(message: str):
    return message

def third_function(any_function):
    return any_function("Hey")

print(third_function(first_function))


#inner functions
def main_function(message: str):
    print(message)

    def inner_function1(message: str):
       print(message)

    def inner_function2(message: str):
        print(message)

    inner_function2("Inner2")
    inner_function1("Inner1")

main_function("MAIN")

#function as return value

def main(message: str):
    def inner1(message: str):
        print("inner1")
    def inner2(message: str):
        print("inner2")

    if message == "hi":
        return inner1
    else:
        return inner2
    
print(main("hi")("hello"))

#question : python -i greeters.py: what -i do
#in repl importimg things from file is possible


#simple decorators

def main_func(func1):
    def wrapper():
        func1()
    return wrapper

def greet():
    print("heyy")

print(main_func(greet))
call_greet = main_func(greet)
print(call_greet)
call_greet()

#Ddecorator syntax

def func(func1):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func1(*args, **kwargs)
    return wrapper

@func
def greet():
    print("hello")

@func
def greet1(message: str):
    print(message)
    return f"new message {message}"

greet()
print(greet1("heyy"))

print(greet.__name__)
print(help(greet))


