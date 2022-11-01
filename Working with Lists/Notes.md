# Working with lists

## Looping Through an Entire List

- You can loop through the entire list using a `for` loop. The general syntax for this loop is shown here:

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
```

## Avoiding Indentation Errors

- Python uses indentation to determine how a line, or group of lines, is related to the rest of the program.
- If you indent a line of code that should not be indented, Python will report an error.

### Types of Identation Errors

- Forgetting to Ident
- Forgetting to Ident Additional Lines
- Indenting Unnecessarily
- Indenting Unnecessarily after the Loop
- Forgetting the Colon

## Making Numerical List

- You can use the `range()` function to generate a series of numbers. The `range()` function starts with the first value you give it and stops when it reaches the second value you provide.

```python
for value in range(1,5):
    print(value)
for value in range(6):
    print(value)
```

### Using range to make a list of numbers

- You can convert the results of `range()` directly into a list using the `list()` function.

```python
numbers = list(range(1,6))
print(numbers)

# skip numbers in a given range, in this case, skip 2 numbers
numbers = list(range(1,21,2))
print(numbers)
```

## List Comprehensions

- A list comprehension allows you to generate this same list in just one line of code.

```python
squares = [value**2 for value in range(1,11)]
print(squares)
```

## Some other Methods

- min() - returns the smallest value in a list
- max() - returns the largest value in a list
- sum() - returns the sum of all the values in a list


## Working with part of a list

### Slicing a list

- You can make a slice, which is a specific group of items in a list. To make a slice, you specify the index of the first and last elements you want to work with.

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
```

- You can include a third value in the brackets indicating a slice. If a third value is included, this tells Python how many items to skip between items in the specified range.

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:4:2])
```

### Copying a List

- You can copy a list by making a slice that includes the entire original list.

```python
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
```

- Doing the following code will tell python to associate the variable to the other variable making it a *reference* or a *new nam* rather than a copy

```python
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods
```

## Tuples

- A tuple looks just like a list except you use parentheses instead of square brackets. Once you define a tuple, you can access individual elements by using each item's index, just as you would for a list.
- Lists work well for storing collections of items that can change throughout the life of a program The ability to modify lists is particularly important whe you're working with a list of users on a website or a list of characters in a game. However, sometimes you'll want to create a list iof items that cannot change. Tuples allow you to do just that. Python refers to values that cannot change as immutable, and an immutable list is called a tuple.

```python
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
```

- Tuples are technically defined by the presense of a comma; the parentheses make them look neater and more readable. If you want to define a tuple with one element, you need to include a trailing comma. `My-t = (3,)`

### Writing over a tuple

- Although you can't modify a tuple, you can assign a new value to a variable that represents a tuple.

```python
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
```
