# Classes

- python classes are objects too and can be assigned to variables and passed as arguments to functions just like any other object.

## Creating and using a Class

- A class is created by the keyword class followed by the name of the class and a colon (:) as follows:

```python
class MyClass:
    pass
```

## Creating a Dog Class

- A class is a blueprint for the object. An object has properties and methods (functions) associated with it. Almost everything in Python is an object, with its properties and methods.

```python
class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")
```

### The __init__() method

- A function that’s part of a class is a method. The __init__() method is a special method that Python runs automatically whenever we create a new instance based on the Dog class. This method has two leading underscores and two trailing underscores, a convention that helps prevent Python’s default method names from conflicting with your method names.

### Making an Instance from a Class

- To make an instance from a class, you give the name of the class, and place parentheses after it. Python will make an instance of the class and store that instance in the variable you provided. The __init__() method is automatically run whenever we create a new instance.

```python
my_dog = Dog('willie', 6)
```

### Accessing Attributes

- To access the attributes of an instance, you use dot notation. You access attributes using an instance name followed by the dot operator and the attribute name.

```python
my_dog.name
my_dog.age
```

### Calling Methods

- To call a method, give the name of the instance and the method you want to call, separated by a dot.

```python
my_dog.sit()
my_dog.roll_over()
```

### Creating Multiple Instances

- You can create as many instances from a class as you need to. Let’s make a second dog, whose name is ‘lucy’ and is 3 years old.

```python
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
```
