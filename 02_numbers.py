# Number

# ---------------------------------

# Interger
# value=20
# print(value)

# type of integer is <class 'int'>
# print(type(value))

# print('we can add two numbers using + operator',5+10)
# print('we can add two multiply using * operator',10*19)
# ---------------------------------

# float
# type of float is - <class 'float'>
floatNumber = 39.819
# print(floatNumber)
# print(type(floatNumber))


print(10 / 2)  # 5.0 (division always returns float in Python 3)

print(10 // 2)  # 5 (floor division returns int)

print(0.1 + 0.2)  # 0.30000000000000004 (floating-point precision limitation)

# The 0.1 + 0.2 result is a known floating-point arithmetic limitation. For financial calculations requiring exact decimal precision, use the decimal module instead.


# ---------------------------------

# complex
# x = 3+5j
# y = 5j
# z = -5j

# print(type(x))
# print(type(y))
# print(type(z))

# ---------------------------------
"""
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

"""
# ------------------------------
"""
z = 3 + 5j

print(type(z)) #<class 'complex'>

print(z.real) # 3.0

print(z.imag) # 5.0

print(abs(z)) # 5.830951894845301 (magnitude)

"""
