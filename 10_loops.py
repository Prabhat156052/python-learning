

## ----------------------------
# for loop

# The `for` loop is used to iterate over an iterable such as a list, tuple, set, string, dictionary, range, etc.


numbers = [10, 20, 30, 40]


for number in numbers:

    print(number)


# Output:

# 10

# 20

# 30

# 40

## ----------------------------
# for loop with string

name = "Python"


for char in name:

    print(char)


# Output:

# P

# y

# t

# h

# o

# n

## ----------------------------
# for loop with tuple and set

mytuple = (10, 20, 30)


for value in mytuple:

    print(value)


myset = {10, 20, 30}


for value in myset:

    print(value)


# Note:

# Set values do not have a guaranteed order.

## ----------------------------
# for loop with dictionary

person = {

    "name": "Prabhat",

    "age": 25,

    "city": "Patna"

}


# Iterate keys

for key in person:

    print(key)


# Iterate values

for value in person.values():

    print(value)


# Iterate both key and value

for key, value in person.items():

    print(key, value)

## ----------------------------
# range() with for loop

# range(stop)

for i in range(5):

    print(i)


# Output:

# 0

# 1

# 2

# 3

# 4


# range(start, stop)

for i in range(2, 6):

    print(i)


# Output:

# 2

# 3

# 4

# 5


# range(start, stop, step)

for i in range(2, 10, 2):

    print(i)


# Output:

# 2

# 4

# 6

# 8

## ----------------------------
# Reverse range

for i in range(5, 0, -1):

    print(i)


# Output:

# 5

# 4

# 3

# 2

# 1

## ----------------------------
# enumerate()

# enumerate() gives both index and value.


fruits = ["apple", "banana", "mango"]


for index, fruit in enumerate(fruits):

    print(index, fruit)


# Output:

# 0 apple

# 1 banana

# 2 mango


# Start index from 1

for index, fruit in enumerate(fruits, start=1):

    print(index, fruit)


# Output:

# 1 apple

# 2 banana

# 3 mango

## ----------------------------
# zip()

# zip() allows us to iterate over multiple iterables together.


names = ["Prabhat", "Rahul", "Amit"]

ages = [25, 26, 24]


for name, age in zip(names, ages):

    print(name, age)


# Output:

# Prabhat 25

# Rahul 26

# Amit 24

## ----------------------------
# Nested for loop

# A loop inside another loop is called a nested loop.


for i in range(3):

    for j in range(2):

        print(i, j)


# Output:

# 0 0

# 0 1

# 1 0

# 1 1

# 2 0

# 2 1

## ----------------------------
# Nested dictionary loop

myfamily = {

    "child1": {

        "name": "A",

        "age": 10

    },

    "child2": {

        "name": "B",

        "age": 12

    }

}


for x, obj in myfamily.items():

    print(x)


    for y, value in obj.items():

        print(y + ':', value)

## ----------------------------
# while loop

# The `while` loop executes as long as its condition is True.


count = 1


while count <= 5:

    print(count)

    count += 1


# Output:

# 1

# 2

# 3

# 4

# 5

## ----------------------------
# break statement

# The `break` statement completely stops the loop.


for number in range(10):

    if number == 5:

        break


    print(number)


# Output:

# 0

# 1

# 2

# 3

# 4

## ----------------------------
# continue statement

# The `continue` statement skips the current iteration and moves to the next iteration.


for number in range(5):

    if number == 2:

        continue


    print(number)


# Output:

# 0

# 1

# 3

# 4

## ----------------------------
# pass statement with loop

# The `pass` statement does nothing. It can be used when the loop body is required but the logic is not written yet.


for number in range(5):

    pass

## ----------------------------
# for-else statement

# The `else` block executes when the `for` loop completes normally.


for number in range(5):

    print(number)

else:

    print("Loop completed")


# If the loop is stopped using break, the else block does not execute.


for number in range(5):

    if number == 2:

        break


    print(number)

else:

    print("Loop completed")

## ----------------------------
# while-else statement

# The `else` block can also be used with a while loop.


count = 1


while count <= 3:

    print(count)

    count += 1

else:

    print("Loop completed")

## ----------------------------
# for vs while

# Use `for` when you want to iterate over an iterable or repeat something a known number of times.


numbers = [10, 20, 30]


for number in numbers:

    print(number)


# Use `while` when repetition depends mainly on a condition.


count = 1


while count <= 5:

    print(count)

    count += 1

## ----------------------------
# Important loop concepts

# Main Python loops

# 1. for loop

# 2. while loop


# Common things used with loops

# 3. range()

# 4. enumerate()

# 5. zip()

# 6. nested loops

# 7. break

# 8. continue

# 9. pass

# 10. for-else

# 11. while-else


# Important:

# A for loop works with any iterable.

# Examples: list, tuple, set, string, dictionary, range, enumerate, zip, etc.