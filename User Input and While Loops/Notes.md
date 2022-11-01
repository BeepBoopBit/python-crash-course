# User Input and While Loops

## How the input() Function Works

- The `input()` function pauses your program and waits for the user to enter some text. Once Python receives the user’s input, it stores it in a variable to make it convenient for you to work with.

```python
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
```

## Using int() to Accept Numerical Input

- The `input()` function takes in everything the user enters, even if they type in a number. If you want to accept numerical input, you’ll need to convert the input to an integer using the `int()` function.

```python
age = input("How old are you? ")
age = int(age)
```

## The Modulo Operator

- The modulo operator returns the remainder of the division of two numbers.

```python
4 % 3
```

## Introduction to while loops

- A `while` loop runs as long as, or while, a certain condition is true.

```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```

## Using break to Exit a loop

- The `break` statement is used to exit a `while` loop.

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
```

## Using continue in a loop

- The `continue` statement returns the loop to the beginning based on the result of a conditional test.

```python
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
```
