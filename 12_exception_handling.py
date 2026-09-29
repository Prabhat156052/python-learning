

## ==== try except else finally ==== ##

# try:
#     res = 10/0
    
# except:
#     print('We can not devie  any thing by 0')  
# We can not devie  any thing by 0

# --------------

# try:
#     num = int(input('enter a num : '))
#     result = 100 / num
#     print('Result==', result)
# except ValueError:
#     print('Inavalid num')

# except ZeroDivisionError:
#     print('cannot be divided by zero')
    
# # enter a num : 5
# # Result== 20.0

# # enter a num : test 
# # Inavalid num

# # enter a num : 0
# # cannot be divided by zero

# try:
#     num = int(input('enter a num : '))
#     result = 100 / num
#     print('Result==', result)
# except ValueError:
#     print('Inavalid num')

# except ZeroDivisionError:
#     print('cannot be divided by zero')
# finally:
#     print('Finally block executed!')
    
# #enter a num : abc
# # Inavalid num
# # Finally block executed!

# # enter a num : 6
# # Result== 16.666666666666668
# # Finally block executed!

# =========== manually generate an exception using raise. ====== #

# a = int(input('Your age: '))
# if a < 18:
#         raise Exception('You are underage')

# # Your age: 14
# # Traceback (most recent call last):
# #   File "c:\Users\91778\Python\12_exception_handling.py", line 58, in <module>
# #     raise Exception('You are underage')
# # Exception: You are underage


# try:
#     x = 10 / 2

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# else:
#     print("Result:", x)
    
# # Result: 5.0


## = Custom Exception === ##

class AgeError(Exception):
    pass

age = 15

try:
    if age < 18:
        raise AgeError("Age must be 18 or above")

except AgeError as e:
    print("Error:", e)
    
# Error: Age must be 18 or above