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

## Using a while loop with lists and dictionaries

### Moving Items from One List to Another

- You can use a `while` loop to move items from one list to another.

```python
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
```

### Removing All Instances of Specific Values from a List

- You can use a `while` loop to remove all instances of a specific value from a list.

```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
```

### Filling a Dictionary with User Input

- You can use a `while` loop to prompt users for input.

```python
responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
```
