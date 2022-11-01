# If Statements

- An if statement is a way to tell Python to take action only if a certain condition is true.

## A Simple Example

- The following example shows how to use an if statement to print a message only if a certain condition is true.

```python
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
```

## Conditional Tests

- At the heart of every if statement is an expression that can be evaluated as True of False and is called a conditional test.

### Checking for Equality

- The most simple conditional test checks whether the value of a variable is equal to the value of interest.

```python
car = 'bmw' # Assignment Operator
car == 'bmw' # Conditional Test
```

### Checking for Inequality

- To check for inequality, you can combine an exclamation point and an equal sign (!=).

```python
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")
```

### Numerical Comparisons

- You can also use comparison operators to compare numbers.

```python
age = 18 # Assignment Operator
age == 18 # Conditional Test
```

- The following table shows all of the comparison operators.

| Operator | Meaning |
|----------|---------|
| ==       | Equal to |
| !=       | Not equal to |
| >        | Greater than |
| <        | Less than |
| >=       | Greater than or equal to |
| <=       | Less than or equal to |

### Checking Multiple Conditions

- The and operator allows you to check multiple conditions at the same time.

```python
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21
```

- The or operator allows you to check multiple conditions at the same time.

```python
age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21
```

### Checking Whether a Value Is in a List

- You can check whether a value is in a list using the in operator.

```python
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
'onions' in requested_toppings
'pepperoni' in requested_toppings
```


