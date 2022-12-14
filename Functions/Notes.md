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

## Returning Values

- A function doesn’t always have to display its output directly. Instead, it can process some data and then return a value or set of values. The value the function returns is called a return value. The return statement takes a value from inside a function and sends it back to the line that called the function.

```python

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
```

### Returning a Simple Value

- The following function returns the full name, neatly formatted.

```python
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
```

### Making an Argument Optional

- You can make an argument optional by giving it an empty default value and then testing for its existence in the body of the function.

```python
def get_formatted_name(first_name, last_name,  middle_name = ' '):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
```

### Returning a Dictionary

- You can return any kind of value you need from a function. For example, you can return a dictionary that contains information about a person you’re describing.

```python
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person
```

### Using a Function with a while Loop

- You can use a function in a while loop to collect as much information as the user wants to enter.

```python
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
```

### Passing a List

- You can pass any kind of information to a function. For example, you can pass a list of names to a function that greets each person in the list.

```python
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
        
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
```

### Modifying a List in a Function

- You can pass a list to a function just as you would any other argument, and the function can work with the list. Any changes the function makes to the list are permanent, allowing you to work efficiently even when you’re dealing with large amounts of data.

```python
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Simulate creating a 3D print from the design.
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
```

### Preventing a Function from MOdifying a List

- To prevent a function from modifying a list, you can pass the function a copy of the list instead of the original list. The slice notation [:] makes this possible.

```python
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Simulate creating a 3D print from the design.
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
```

## Passing an Arbitrary Number of Arguments

- Sometimes you won’t know ahead of time how many arguments a function needs to accept. Python allows a function to collect an arbitrary number of arguments from the calling statement.

```python
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    for topping in toppings:
        print(f"- {topping}")
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

- The asterisk in the parameter name *toppings tells Python to make an empty tuple called toppings and pack whatever values it receives into this tuple. The print statement in the function body produces output showing that Python can handle a function call with one value and a call with three values.

### Mixing Positional and Arbitrary Arguments

- If you want a function to accept several different kinds of arguments, the parameter that accepts an arbitrary number of arguments must be placed last in the function definition. Python matches positional and keyword arguments first and then collects any remaining arguments in the final parameter.

```python
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

### Using Arbitrary Keyword Arguments

- Sometimes you’ll want to accept an arbitrary number of arguments, but you won’t know ahead of time what kind of information will be passed to the function. In this case, you can write functions that accept as many key-value pairs as the calling statement provides.

```python
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
```

- The double asterisks before the parameter **user_info cause Python to create an empty dictionary called user_info and pack whatever name-value pairs it receives into this dictionary. This dictionary is then passed to the function.

## Storing your Functions in Modules

- A module is a file ending in .py that contains the code you want to import into your program. You can store your functions in a separate file called a module and then import that module into your main program. You can also store your functions in a module and then import specific functions you want into your main program.

### Importing an Entire Module

- To start importing functions, we first need to create a module. A module is a file ending in .py that contains the code you want to import into your program. Let’s make a module that contains the functions we wrote for making pizza. We’ll call this module pizza.py.


```python
# pizza.py
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
```

```python
# making_pizzas.py
import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

### Importing Specific Functions

- You can also import a specific function from a module. Here’s the general syntax for this approach:

```python
from module_name import function_name
from module_name import function_0, function_1, function_2
```

### Using as to Give a Function an Alias

- You can also provide an alias for a function while importing it. An alias is an alternate name for a function or class that you can use to simplify your code. Here’s the general syntax for this approach:

```python
from module_name import function_name as fn
```

### Using as to Give a Module an Alias

- You can also provide an alias for a module name. Here’s the general syntax for this approach:

```python
import module_name as mn
```

### Importing All Functions in a Module

- You can tell Python to import every function in a module by using the asterisk (*) operator. Here’s the general syntax for this approach:

```python
from module_name import *
```

