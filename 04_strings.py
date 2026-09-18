# We will practice string here
# --------------------------------------
# name = "Prabhat"

# city = 'Patna'

message = "Welcome to Paython Learning"

# paragraph = """This is a

# multi-line string."""

# print(type(name)) # <class 'str'>

# print(paragraph)

# a = "Hello, World!"
# print(a[1])

# print("Lopping str through for loop")
# for x in "World":
#     print(x)

# --------------------------------------

course = "digital marketing"

# if 'digital' in course: # in keyword return true if found the phrase/char
#     print("Digital found in Course string\n")
# if 'Book' not in course: # not in keyword to check if searched is not in string
#     print('Book not found in course\n')
# print('Upper case:',course.upper()) # DIGITAL MARKETING

# print(course.capitalize()) # Digital marketing

# print(course.replace("digital", "advanced")) # advanced marketing

# print(len(course)) # 16

print(course.split(" ")) # ['digital', 'marketing']

# print(course.strip()) # removes leading/trailing spaces

# print(course.startswith("digital")) # True
# print(course.endswith("marketing")) # True

# print(course.count("i")) # 3


# print(message.find('Python')) #11 (return the first index where it belong, and return -1 if not found)
# print(message.find('digital')) #-1
# username = "Prabhat"

# if username.isalpha():
#     print("Valid username")
    
# otp = '126648'

# if otp.isdigit():
#     print("OTP contains only digits")

# text = "   "

# if text.isspace():
#     print("Input contains only spaces")

# replace-(all occurences of Learning will be replaced by Course)
# newMessage = message.replace('Learning', 'Course') # Welcome to Paython Course 
# print(newMessage,'\n')

# splitedMessage = newMessage.split(' ');

# numbers = [10, 20, 30]

# string_numbers = list(map(str, numbers))

# print(string_numbers)
# # ['10', '20', '30']

# result = "-".join(string_numbers)

# print(result) # 10-20-30

# result = "-".join(map(str, numbers))

# print(result) #10-20-30

text = 'Welcome'
print(text[1:5]) #elco
print(text[1:]) #elcome
print(text[0:]) #Welcome
print(text[-3:]) #ome