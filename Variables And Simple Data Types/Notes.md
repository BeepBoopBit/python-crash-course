# Chapter 2

## Variables

- Every variable is connected to a value, which is the information associated with the value
- Variable names can contain letters, numbers, and underscores. They can start with a letter or an underscore, but not with a number.
- Space are not allowed in vairable names.
- Avoid using Python keyword and function names as variable names, that is, do not use words that Python has reserved for a particular programmatic purpose, such as the word print.
- Variable names should be short but descriptive.
- Be careful when using the lowercase letter l and the uppercase letter O because they could be confused with the numbers 1 and 0.

## Variables as Labels

- It is helpful to think of variables as labels that you can assign to values. You can also say that a variable references a certain value.

## Traceback

- A traceback is a list of the functions that were executing when the error occurred.
- The interpreter provides a traceback when a program cannot run successfuly

## Strings

- A series of characters. Anythign inside quotes is considered a string in Python, and you can use single or double quotes around your string.
- This flexibility allows you to use quotes and apostrophes within your strings.

### What is a method?

- A method is an action that Python can perform on a piece of data. Every method is followed by a set of parentheses, because methods often need additional information to do their work. This information is provided inside the parentheses.

### String methods

- title() - Capitalizes the first letter of each word in a string
- upper() - Converts a string to uppercase letters
- lower() - Converts a string to lowercase letters
- rstrip() - Removes whitespace temporarily from the right side of a string
- lstrip() - Removes whitespace temporarily from the left side of a string
- strip() - Removes whitespace temporarily from both sides of a string

## Using Variables in String

```python
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
```

- The f before the quotation marks tells Python to interpret the contents of the string literally, and to replace the name of any variable in braces with its value.
- These strings are called f-strings. The f is for format, because Python formats the string by replacing the name of any variable in braces with its value.

### Python 3.5 or later

- You should use format() method instead of f-strings. This is because f-strings are not supported in Python 3.4 or earlier.

```python
full_name = "{} {}".format(first_name, last_name)
```
# Numbers

## Integers

- Integers are whole numbers with no decimal point.

## Floats

- Floats are numbers with a decimal point.
- Python calls any number with decimal point a float, even if there are no digit after the decimal point.
- This term is used in most programming language, and it refers to the fact that a decimal point can appear at any position in a number.


## Integer and Floats

- When you divide any two numbers, even if they are integers. It always results in a float.
- If you mix an integer and a float in any other operation, you'll get a float as well.
- Python defaults to a float in any operation that uses a float, even if the output is a whole number.


## Underscores in Numbers

- You can use Underscores when writing long numbers to make them easier to read.

```python
some_number = 12_003_412
```

## Multiple Assignments

- You can assign values to more than one variable using just one line.

```python
x,y,z = 0,0,0
```

## Constants

- A constant is like a variable whose value stays the same throughout the life of a program. Python convention is to use all capital letters for constants.

## Comments

- Comments are notes you add to your program to explain it in plain English. Python ignores comments when running your program.

```python
# This will print watermelon
print("watermelon")
```