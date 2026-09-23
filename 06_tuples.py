tuple_example = (1,2,3,4)
# print(type(tuple_example)) #<class 'tuple'>

# tuple_single_value= (1,)  #comma required 
# print(tuple_single_value) #(1,)

# print(tuple_example) #(1,2,3,4)
# print(len(tuple_example)) #4
# print(tuple_example[1]) #2
# print(tuple_example[-1]) #4
# print(tuple_example[1:3]) #(2,3)

# tuple1 = ("apple", "banana", "cherry")
# tuple2 = (1, 5, 7, 9, 3)
# tuple3 = (True, False, False)
# tuple4 = ("abc", 34, True, 40, "male")
# print(tuple1) #("apple", "banana", "cherry")
# print(tuple2) #(1, 5, 7, 9, 3)
# print(tuple3) #(True, False, False)
# print(tuple4) #("abc", 34, True, 40, "male")

# thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# # print(thistuple) #("apple", "banana", "cherry")


# print("apple" in thistuple) #True

#--------------------------------
# tuple1 = ("apple", "banana", "cherry")

# # Adding any value to tuple using list

# list1= list(tuple1) #converted to list

# list1.append('yellow') 

# tuple1 = tuple(list1) #conveted back to tuple

# print(tuple1) #("apple", "banana", "cherry", "yellow")

# # Adding any value to tuple using another list
# tuple2 = ("apple", "banana", "cherry")

# tuple3 = ("green",)

# tuple2+=tuple3
# print(tuple2) #("apple", "banana", "cherry", "green")

#--------------------------------

#Remove Items from tuple

# removing any value to tuple using list

# tuple4 =("apple", "banana", "cherry", "green")

# list2 = list(tuple4)

# list2.remove("banana")

# tuple4=tuple(list2)
# print(tuple4)  #('apple', 'cherry', 'green')

# using del keyword

# tuple5= (1,2,3,4,5)

# del tuple5
# print(tuple5) #NameError: name 'tuple5' is not defined. Did you mean: 'tuple'?

#----------------------------------

#unpacking tuples

# fruits = ("apple", "banana", "cherry")

# (apple, banana, blue) = fruits

# print(apple) #apple
# print(banana) #banana
# print(blue) #cherry

# fruits2=  ("apple", "mango", "papaya", "pineapple", "cherry")

# (one , *two, three) = fruits2

# print(one)
# print(two)
# print(three)

#--------------------------          

# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3) #('a', 'b', 'c', 1, 2, 3)

tuple1 = ("a", "b" , "c")

# for x in tuple1:
#     print(x)
    
# for i in range(len(tuple1)):
#     print(tuple1[i])

i=0
while i < len(tuple1):
    print(tuple1[i])
    i+=1

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple) #('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')




