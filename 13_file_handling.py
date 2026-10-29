
# ============================================================
# PYTHON FILE HANDLING — COMPLETE NOTES (UP TO WRITING)
# ============================================================

# File handling allows us to create, read, write, and update files.
# Common functions: open(), read(), readline(), readlines(),
# write(), writelines(), seek(), tell(), truncate(), close()


# ============================================================
# 1. OPEN A FILE AND READ ITS CONTENT
# ============================================================

# 'r' = read mode. The file must already exist.

with open('abc.txt', 'w', encoding='utf-8') as f:
    f.write(
        'This is an example to show how to open a file and read.\n'
        'This is the second line of the text.'
    )

f1 = open('abc.txt', 'r', encoding='utf-8')

print(type(f1))
# Output: <class '_io.TextIOWrapper'>
# f1 is a file object, not the actual file content.

text = f1.read()

print(text)
# Output:
# This is an example to show how to open a file and read.
# This is the second line of the text.

print(type(text))
# Output: <class 'str'>
# read() returns the file content as a string.

f1.close()


# ============================================================
# 2. WRITE AND READ USING r+ MODE
# ============================================================

# 'r+' = read + write.
# The file must exist.
# Existing content is NOT automatically deleted.

with open('abc.txt', 'w', encoding='utf-8') as f:
    f.write('Original file content.')

f = open('abc.txt', 'r+', encoding='utf-8')

print(f)
# Output resembles:
# <_io.TextIOWrapper name='abc.txt' mode='r+' encoding='utf-8'>

f.write('Hello Python')
# Writes from the current position, initially position 0.
# Existing characters at these positions are overwritten.

print('After write:', f.tell())
# Output: After write: 12
# The pointer is now after the 12 characters written.

f.seek(0)
# Move the pointer to the beginning.

print('File content:', f.read())
# Output: File content: Hello Pythontent.
# The first 12 characters were replaced; the old suffix remains.

f.close()


# ============================================================
# 3. CREATE A FILE AND WRITE MULTIPLE LINES
# ============================================================

# 'w' = write mode.
# Creates the file if it does not exist.
# If it exists, its previous content is truncated.

file_obj = open('newFile1.tsx', 'w', encoding='utf-8')

file_obj.write('Hello Python\n')
file_obj.write('I am learning file handling\n')
file_obj.write('This is my new comment')

file_obj.close()

# Read the file using a new file handle.
file_obj1 = open('newFile1.tsx', 'r', encoding='utf-8')

print(file_obj1.read())
# Output:
# Hello Python
# I am learning file handling
# This is my new comment

file_obj1.close()


# ============================================================
# 4. READ A SPECIFIC NUMBER OF CHARACTERS
# ============================================================

with open('newFile1.tsx', 'r', encoding='utf-8') as f:
    print(f.read(4))
    # Output: Hell

    print(f.read(4))
    # Output: o Py
    # Reading continues from the current pointer position.

    print(f.read(-1))
    # Output:
    # thon
    # I am learning file handling
    # This is my new comment
    #
    # read(-1) reads all remaining content.
    # It is equivalent to read() with no argument.

    print(repr(f.read()))
    # Output: ''
    # The pointer has reached the end of the file.


# ============================================================
# 5. READ ONE LINE USING readline()
# ============================================================

with open('newFile1.tsx', 'r', encoding='utf-8') as f:
    print(repr(f.readline()))
    # Output: 'Hello Python\n'

    print(repr(f.readline()))
    # Output: 'I am learning file handling\n'

    print(repr(f.readline()))
    # Output: 'This is my new comment'

    print(repr(f.readline()))
    # Output: ''
    # An empty string indicates the end of the file.

# readline() retains the newline character when present.
# repr() makes newline characters visible in the output.


# ============================================================
# 6. AVOID EXTRA BLANK LINES WHILE PRINTING
# ============================================================

with open('newFile1.tsx', 'r', encoding='utf-8') as f:
    line = f.readline()
    print(line)
    # The line already ends in '\n'.
    # print() adds another newline, so an extra blank line appears.

with open('newFile1.tsx', 'r', encoding='utf-8') as f:
    line = f.readline()
    print(line, end='')
    # Avoids adding an additional newline.

# Another option:
with open('newFile1.tsx', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')


# ============================================================
# 7. READ ALL LINES USING readlines()
# ============================================================

with open('abc.txt', 'w', encoding='utf-8') as f:
    f.write(
        'This is an example to show how to open a file and read.\n'
        'This is the second line of the text.'
    )

with open('abc.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(lines)
# Output:
# ['This is an example to show how to open a file and read.\n',
#  'This is the second line of the text.']

print(type(lines))
# Output: <class 'list'>

print(lines[0])
# Output:
# This is an example to show how to open a file and read.

print(lines[1])
# Output:
# This is the second line of the text.

# readlines() returns a list of strings.
# Newline characters are retained when present.


# ============================================================
# 8. LOOP THROUGH FILE LINES
# ============================================================

with open('abc.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')

# Output:
# This is an example to show how to open a file and read.
# This is the second line of the text.

# Iterating directly over a file is generally memory-efficient
# for large text files because it processes one line at a time.


# ============================================================
# 9. tell() AND seek()
# ============================================================

with open('abc.txt', 'r', encoding='utf-8') as f:
    print(f.tell())
    # Output: 0
    # Initial position is at the beginning.

    print(f.read(5))
    # Output: This

    print(f.tell())
    # Output: 5
    # Position after reading five ASCII characters.

    f.seek(0)
    # Move the pointer back to the beginning.

    print(f.tell())
    # Output: 0

    print(f.read(5))
    # Output: This

# tell() returns the current stream position.
# seek(0) moves the position to the beginning.
# read() continues from the current position.


# ============================================================
# 10. WRITE MULTIPLE LINES USING writelines()
# ============================================================

lines = [
    'Hello Python\n',
    'Welcome to file handling\n',
    'Learning file writing\n'
]

with open('abc.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)

# writelines() writes each string in the iterable.
# It does NOT insert newline characters automatically.
# That is why each string above contains '\n'.

with open('abc.txt', 'r', encoding='utf-8') as f:
    print(f.read())

# Output:
# Hello Python
# Welcome to file handling
# Learning file writing


# ============================================================
# 11. WRITE NUMBERS INTO A FILE
# ============================================================

# write() accepts a string, not an integer.

with open('newFile1.tsx', 'w', encoding='utf-8') as f:
    f.write(str(100))
    f.write('\n')
    f.write(str(2000))

# Read back the content.
with open('newFile1.tsx', 'r', encoding='utf-8') as f:
    print(f.read())

# Output:
# 100
# 2000

# This causes a TypeError:
# f.write(2000)
# TypeError: write() argument must be str, not int

# Using an f-string is also valid:
with open('newFile1.tsx', 'w', encoding='utf-8') as f:
    age = 25
    f.write(f'Age: {age}')

with open('newFile1.tsx', 'r', encoding='utf-8') as f:
    print(f.read())

# Output: Age: 25


# ============================================================
# 12. APPEND CONTENT USING 'a' MODE
# ============================================================

# 'a' = append mode.
# New content is written at the end.
# Creates the file if it does not exist.

with open('abc.txt', 'a', encoding='utf-8') as f:
    f.write('New line added\n')

with open('abc.txt', 'r', encoding='utf-8') as f:
    print(f.read())

# The new line appears after the existing content.


# ============================================================
# 13. UPDATE CONTENT USING r+ AND truncate()
# ============================================================

with open('abc.txt', 'w', encoding='utf-8') as f:
    f.write('Hello Python\nWelcome')

with open('abc.txt', 'r+', encoding='utf-8') as f:
    f.seek(0)
    f.write('Hi')

# File content:
# Hillo Python
# Welcome

# Only the first two characters were replaced.

with open('abc.txt', 'r+', encoding='utf-8') as f:
    f.seek(0)
    f.write('Hello')
    f.truncate()

with open('abc.txt', 'r', encoding='utf-8') as f:
    print(f.read())

# Output: Hello
# truncate() removes the content after the current position.


# ============================================================
# 14. 'w+' MODE — WRITE AND READ
# ============================================================

# 'w+' creates a file if missing and truncates it if it exists.

with open('abc.txt', 'w+', encoding='utf-8') as f:
    f.write('Python Developer')

    f.seek(0)
    print(f.read())

# Output: Python Developer


# ============================================================
# 15. 'a+' MODE — APPEND AND READ
# ============================================================

# 'a+' preserves existing content and writes at the end.
# seek(0) allows us to read from the beginning.

with open('abc.txt', 'a+', encoding='utf-8') as f:
    f.write('\nReact Developer')

    f.seek(0)
    print(f.read())

# Output:
# Python Developer
# React Developer


# ============================================================
# 16. WHY use 'with open()'?
# ============================================================

# Preferred approach:
with open('abc.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)

# The file closes automatically when the with block exits.
# This is safer than manually calling f.close() in every case.

# You can still use:
# f = open('abc.txt', 'r', encoding='utf-8')
# try:
#     print(f.read())
# finally:
#     f.close()


# ============================================================
# END OF FILE HANDLING NOTES — READING AND WRITING
# ============================================================
