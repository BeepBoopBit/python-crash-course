# FUnctions

## Defining a Function

- A function is a block of code that you can give a name and then call to execute the code in the block whenever you need to.

```python
def greet_user():
    """Display a simple greeting."""
    print("Hello!")
```

## Passing Information to a Function

- Information that’s passed from a function call to a function is called an argument.

```python
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")
```

## Arguments and Parameters

- A parameter is a piece of information the function needs to do its job. The argument is a piece of information that is passed from a function call to a function. A parameter is the variable listed inside the parentheses in the function definition. An argument is the value that is sent to the function when it is called.

```python
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")
```

## Passing arguments

- You can pass arguments to a function in a number of ways. You can use positional arguments, which need to be in the same order the parameters were written, keyword arguments, which associate each argument with a parameter name, and lists and dictionaries of values.

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
```

### Positional Arguments

- Positional arguments need to be in the same order the parameters were written.

```python
describe_pet('hamster', 'harry')
```

### Multiple Function Calls

- You can call a function as many times as needed.

```python
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
```

### Keyword Arguments

- Keyword arguments are associated with each parameter name.

```python
describe_pet(animal_type='hamster', pet_name='harry')
```

### Default Values

- You can define a default value for each parameter. If an argument for a parameter is provided in the function call, Python uses the argument value. If not, it uses the parameter’s default value.

```python
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
```

- When you use default values, any parameter with a default value needs to be listed after all the parameters that don't have default values. This allows python to continue interpreting positional arguments correctly.


### Equivalent Function Calls

- The following function calls would all give the same output.

```python
describe_pet('willie')
describe_pet(pet_name='willie')
describe_pet(animal_type='dog', pet_name='willie')
```
