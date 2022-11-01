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

### Checking Whether a Value Is Not in a List

- You can check whether a value is not in a list using the not in operator.

```python
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
```

### Boolean Expressions

- A boolean expression is just another name for a conditional test. A boolean value is either True or False.

```python
game_active = True
can_edit = False
```

## Simple If Statements

- An if statement is a simple way to test for a condition and respond appropriately.

```python
age = 19

if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
```

## If-Else Statements

- An if-else statement allows you to take one action when a condition is true and another action in all other cases.

```python
age = 17

if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
```

## If-Elif-Else Chain

- Python does not require an else block at the end of an if-elif chain. Sometimes an else block is useful; sometimes it is clearer to use an additional elif statement that catches the specific condition of interest.

```python
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
```

## Using multiple elif Blocks

- Python does not limit the number of elif blocks in an if-elif-else chain. You can use as many elif blocks as you need.

```python
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print(f"Your admission cost is ${price}.")
```

