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