
## ----------------------------
# if statement
a= 10
# if(a==10):
#     print('A is 10') # A is 10
# b= True
# if(b):
#     print("b is True") # b is True
    
## elif statement --------

x= 10
y=12

# if(x==y):
#     print('X is equal to y')
# elif(x<y):
#     print('Y is greater than X') # Y is greater than X
    
## else statement -------------

p = 10
q = 20

# if(p > q):
#     print('P is greater')
# elif(p==q):
#     print('Both are equals')
# else:
#     print('Q is greater') # Q is greater

# --------------------------------#
## And , OR, NOT keyword 

a1= 14
a2=30
a3=17

if((a1<a2) and a2 > a3):
    print('And operator test') # And operator test

if((a1>a2) or a2 > a3):
    print('OR operator test') # OR operator test

if( not a1 > a2):
    print('Not operator test') # Not operator test
    
    
#---------------------------------#
if(True):
    pass # pass keyword used with if satement in case if statemet is required but the if block logic is not yet decided,

## ----------------------
age = 25
has_id = True

if age >= 18:
    if has_id:
        print("Allowed") # Allowed
    else:
        print("ID required")
else:
    print("Not allowed")

# -------------------------------
age = 20

if age >= 18: print("Adult") # Adult

# -------------------------

age = 20

result = "Adult" if age >= 18 else "Minor"

print(result) # Adult

fruits = ["apple", "banana", "mango"]

if "apple" in fruits:
    print("Apple exists") # Apple exists
    
if "orange" not in fruits:
    print("Orange does not exist") # Orange does not exist


value = None

if value is None:
    print("No value") # No value

sum = 0
for i in range(5):
    if i == 2:
        continue
    sum +=i
print(sum)  # 8
