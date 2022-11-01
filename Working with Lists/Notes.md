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
