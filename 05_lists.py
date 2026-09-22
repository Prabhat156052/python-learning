items = [12, 14, 16, 20, 25]
mylist = ["apple", "banana", "cherry"]
# print('List:-', mylist)

# print(mylist[-1]) #cherry

# copyList= items
# print('copy:-', copyList)
# copyList.append(24)

# print('\nList:-', items)
# print('\ncopy:-', copyList)

# print(items[1:3]) #[14,16]

# sum=0
# for item in items:
#     sum+=item
# print("Sum of the items items:--", sum) # 87

# numbers = list((1,2,3,4,5))
# print(numbers) # [1,2,3,4,5]

# numbers = list(range(3))
# print(numbers) #[0,1,2]

# rangeList = list(range(4,10)) #range with start and stop
# print(rangeList) #[4, 5, 6, 7, 8, 9]

# rangeList = list(range(7,5))
# print(rangeList) #[]

# rangeWithStepList = list(range(0,11,2)) #range with step
# print(rangeWithStepList) #[0, 2, 4, 6, 8, 10]

# range_reverse_list = list(range(10,0,-2)) 
# print(range_reverse_list)  #[10, 8, 6, 4, 2]


# a = ['one', 'two', 'three']
# i=0
# while i < len(a):
#     print(a[i])  #one two three
#     i+=1

#-----------------------------------------
#items = [12, 14, 16, 20, 25]

# items.insert(2,10)
# print(items) #[12, 14, 10, 16, 20, 25]

# items2= [7,9]
# items.extend(items2) #items = [12, 14, 16, 20, 25]
# print(items)  #[12, 14, 16, 20, 25, 7, 9]

# print(items.index(16)) #2
# items.remove(14)
# print(items) #[12, 16, 20, 25]
# print(items.remove(31)) #ValueError: list.remove(x): x not in list

# items3 = [15, 11, 3, 20, 25, 7, 9]
# charList = ['one', 'two', 'three','four']
# items3.sort()
# print(items3) #[3, 7, 9, 11, 15, 20, 25]

# charList.sort()
# print(charList) #['four', 'one', 'three', 'two']

#Sort in descending order
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True) 
# print(thislist) #['pineapple', 'orange', 'mango', 'kiwi', 'banana']

# thislist_caseSensitive = ["banana", "Orange", "Kiwi", "cherry"]
# thislist_caseSensitive.sort(key = str.lower)
# print(thislist_caseSensitive)  #['banana', 'cherry', 'Kiwi', 'Orange']


# popList = ['one', 'two', 'three','four']

# print(popList.pop(1)) #two
# print(popList.pop()) #four

# delList = [1,3,5,9,6,8]
# del delList[2]
# print(delList) #[1, 3, 9, 6, 8]

# clearList= [1, 3, 9, 6, 8]

# clearList.clear()
# print(clearList) #[]

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy() #shallow copy
# print(mylist) #["apple", "banana", "cherry"]


#copy using slice operator
# thislist_usingSlice = ["apple", "banana", "cherry"]
# mylist = thislist_usingSlice[:]
# print(mylist) #['apple', 'banana', 'cherry']

#accessing index + value 

# using range method
# names = ['one', 'two', 'three']

# for i in range(len(names)):
#     print(i, names[i])
    
# out will be--
# 0 one
# 1 two
# 2 three

#using enumerate
# names = ['one', 'two', 'three']

# for i, name in enumerate(names):
#     print(i, name)
    
# out will be--   
# 0 one
# 1 two
# 2 three

#using zip - it combines multple iterables
names = ['one', 'two', 'three']
numbers = [1, 2, 3]

for name, number in zip(names, numbers):
    print(name, number)

# out will be--      
# one 1
# two 2
# three 3


numbers = [10, 20, 30, 40]

print(min(numbers))  # 10
print(max(numbers))  # 40
print(sum(numbers))  # 100

numbers = [2, 4, 6, 8]

#any() → at least one item is True
print(any(x > 5 for x in numbers))  # True

#all() → every item is True.
print(all(x % 2 == 0 for x in numbers))  # True