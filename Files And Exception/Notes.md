# Files and Exceptions

## Reading from a file

- `open()` function opens a file and returns a file object

### Readign an Entire File

- `read()` method reads the entire contents of the file

```python
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
```

- Python looks for the file provided in the open() argument in the directory where the program that's currently being executed is stored.

### File Paths

- Absolute file path: specifies a location in relation to the root directory of the file system
- Relative file path: specifies a location in relation to the program's current working directory
- `os` module provides functions for interacting with the operating system

```python
import os
os.getcwd()
```

- Windows systems use a backslash '\' instead of a forward slash '/' when displaying file baths, but you can still use forward slashes in your code.


### Reading Line by Line

- `readlines()` method reads each line from the file and stores it in a list

```python
with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line)
```

### Making a list of lines from a file

- `readlines()` method stores the lines in a list

```python
with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()
```

### Working with a File's Contents

- `rstrip()` method removes the whitespace from the right side of a string

```python
with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))
```

- When python reads from a text file, it interprets all text in the file as a string.
- If you read in a number and want to work with that value in a numerical context, you'll have to convert it to an integer using the 'int()' function or convert it to a float using the 'float()' function.

## Writing to a File

- `write()` method writes a string to the file

```python
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
```

- The 'w' argument tells python that we want to open the file in write mode
- The 'r' argument tells python that we want to open the file in read mode
- The 'a' argument tells python that we want to open the file in append mode

## Exceptions

- An exception is an error that occurs while a program is running
- Exceptions are handled with try-except blocks. The code that might cause an exception is put in a try block. The code that should execute if an exception occurs goes in the except block.

```python
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

### the else block

- The code that should run only if the try block was successful goes in the else block.

```python
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
```


### Handling the FileNotFoundError exception

- The FileNotFoundError exception is raised when python can't find a file

```python
filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
```

### Analyzing Text

- The `split()` method breaks a line into a list of words

```python
filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
```

### Working with multiple files

- This is not in the book
- The `glob` module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell

```python
import glob
filenames = glob.glob('*.txt')
for filename in filenames:
    print(filename)
```

## Storing Data

### Using json.dump() and json.load()

- The `json.dump()` function takes two arguments: a piece of data to store and a file object it can use to store the data
- The `json.load()` function takes a single argument: the file object it needs to read data from

```python
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
```

```python
import json

filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj) # ['2', '3', '5', '7', '11', '13']

print(numbers)
```

### Saving and Reading User-Generated Data

- The `input()` function pauses your program and waits for the user to enter some text

```python
import json
username = input("What is your name? ")
filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")
```

```python
import json
filename = 'username.json'
with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")
```