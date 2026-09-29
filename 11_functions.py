# # function in python:-  

# def myFun():
#     print('Hey, Calling from My function')
    
# myFun() # Hey, Calling from My function

# # with parameters/arguments --------
# def myFun(name):
#     print(name)

# myFun('Harry') # Harry

# # returning any value ----------
# def sum(a,b):
#     return(a+b)
# result = sum(5,9)
# print(result) # 14

# # deafult value --------------

# def myFun(name='Neha'):
#     print(name)

# myFun('Shiva') # Shiva
# myFun()     # Neha


# # returning many value -------
# def func():
#     return (17, 'Hello')

# x,c= func()
# print(x) # 17
# print(c) # Hello

# # keyword argument / kwargs : calling function with key name

# def func(name, age):
#     print(name,age)

# func(name='Neha', age =28) # Neha 28

# # positional argument -- calling function without key name

# def func(name, age):
#     print(name,age)

# func("Pavan", 38) # Pavan 38


# # keyword-only argument : # allwoed keyword argument , * is used bofore agrs

# def func(*, name, age ):
#     print(name,age)

# func(name='Neha', age =28) # Neha 28


# # positional-only argument : # allwoed positional argument , / is used after agrs

# def func(name, age,/):
#     print(name,age)

# func("Pavan", 38) # Pavan 38


# # Combining Positional-Only and Keyword-Only
# def my_function(a, b, /, *, c, d):
#   return a + b + c + d

# result = my_function(5, 10, c = 15, d = 20)
# print(result) # 50


 
## Python *args and **kwargs ------------------

#  Arbitrary Arguments - *args

# def myFunction(*friends):
#     print('type of agrs--', type(friends)) # <class 'tuple'>
#     print(friends) # ('Shiva', 'Neha', 'Sakshi')
#     print('second friends:-', friends[1]) # second friends:- Neha

# myFunction('Shiva', 'Neha', 'Sakshi')


# combine regular parameters with *args.

# Regular parameters must come before *args:---

# def my_function(greeting, *names):
#   for name in names:
#     print(greeting, name)

# my_function("Hello",'Shiva', 'Neha', 'Sakshi')

# Hello Shiva
# Hello Neha6
# Hello Sakshi

# **kwargs ------------------

# def my_function(**myvar):
#   print("Type:", type(myvar))
#   print("Name:", myvar["name"])
#   print("Age:", myvar["age"])
#   print("All data:", myvar)

# my_function(name = "Tobias", age = 30, city = "Bergen")
# Type: <class 'dict'>
# Name: Tobias
# Age: 30
# All data: {'name': 'Tobias', 'age': 30, 'city': 'Bergen'}

# Combining *args and **kwargs -----------------

# def my_function(title, *args, **kwargs):
#   print("Title:", title)
#   print("Positional arguments:", args)
#   print("Keyword arguments:", kwargs)

# my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

# Title: User Info
# Positional arguments: ('Emil', 'Tobias')
# Keyword arguments: {'age': 25, 'city': 'Oslo'}

## Using * to unpack a list into arguments:------
# def my_function(a, b, c):
#   return a + b + c

# numbers = [1, 2, 3]
# result = my_function(*numbers) # Same as: my_function(1, 2, 3)
# print(result) # 6

## scope ---------------

# def myfunc():
#   x = 300
#   print(x)

# myfunc() # 300

# def myfunc():
#   x = 300
#   def myinnerfunc():
#     print(x)
#   myinnerfunc()

# myfunc() # 300

x = 300

# def myfunc():
#   x = 200
#   print(x) 

# myfunc() # 200

# print(x) # 300


# Decorator ----------------------- #
#without argument
# def greeting(function):

#     def wrapper():
#         print("Hello,", end=' ')

#         function()

#     return wrapper


# @greeting
# def user():
#     print("Neha")


# user()  # Hello, Neha


#multple decorators call

# def myDecorators(function):
#   def wrapper():
#     print('Hello, Aman', end=' ')
#     function()
#   return wrapper

# @myDecorators
# def mornigGreeting():
#   print('Good Morning')

# @myDecorators
# def eveningGreeting():
#   print('Good Eveneing')

# mornigGreeting() # Hello, Aman Good Morning
# eveningGreeting() # Hello, Aman Good Eveneing


# with argument in decorated funtion

# def greeting(function):
#     def wrapper(name):
#         print("Hello,", end=' ')

#         function(name)

#     return wrapper


# @greeting
# def user(name):
#     print(name)
    
# user('Shiva') # Hello, Shiva
# user('Sakshi') # Hello, Sakshi

## argument in decorator
# def myDecorator(num):
#   def greeting(function):
#       def wrapper(name):
#         print("Hello,", end=' ')
#         for n in range(num): 
#          function(name)

#       return wrapper
#   return greeting

# @myDecorator(3)
# def user(name):
#     print(name)

# user("Sam")

# # Output--
# # Hello, Sam
# # Sam
# # Sam

# #Lambda Functions----------------

# Sum = lambda a,b: a+ b
# result = Sum(14,7)

# print(result)  # 21


# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(11)) # 22

# ----------- with built in function
# numbers = [1, 2, 3, 4, 5]
# doubled = list(map(lambda x: x * 2, numbers))
# print(doubled)  # [2, 4, 6, 8, 10]


# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
# print(odd_numbers) # [1, 3, 5, 7]

# students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
# sorted_students = sorted(students, key=lambda x: x[1])
# print(sorted_students) # [('Tobias', 22), ('Emil', 25), ('Linus', 28)]


###============== generator ========= ###

# def numbers():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5

# result = numbers()

# print(result)  # <generator object numbers at 0x00000235F67D5480>
# print(next(result))
# print(next(result))
# print(next(result))

# # 1
# # 2
# # 3

#------

def numbers():
    for i in range(1, 6):
        yield i

result = numbers()

for num in result:
    print(num)

# 1
# 2
# 3
# 4
# 5