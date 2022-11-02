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
## Working with Classes and Instances

- The Dog class we just created is a fairly simple class, but it demonstrates the basic structure of a class. Let’s look at a few more features of classes.
  
### The Car Class

- Let’s write a class that represents a car. We’ll store information about the kind of car we’re working with and we’ll have a method that summarizes this information. We’ll write one version of the class that has no default values for any of the attributes and a second version that specifies default values for some of the attributes.

```python
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
```

### Setting a Default value for an Attribute

- When an instance is created, attributes can be defined without being passed in as parameters. These attributes can be defined in the __init__() method, where they are assigned a default value.

```python
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """
        Initialize attributes to describe a car.
        Set default value for odometer reading.
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
```

### Modifying an Attribute’s Value Directly

- You can modify an attribute’s value in three ways: you can change the value directly through an instance, set the value through a method, or increment the value (add a certain amount to it) through a method.

```python
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
```

### Modifying an Attribute’s Value Through a Method

- You can define a method that updates each attribute individually or define a method that updates several attributes at once.

```python
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()
```

### Incrementing an Attribute’s Value Through a Method

- You can define a method that increments an attribute’s value by a certain amount.

```python
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
```

## Inheritance

- When you write classes, you’ll sometimes find that you’re writing a class that is a specialized version of another class you wrote. You can use inheritance when you write classes that are similar. When one class inherits from another, it automatically takes on all the attributes and methods of the first class. The original class is called the parent class, and the new class is the child class. The child class inherits every attribute and method from its parent class but is also free to define new attributes and methods of its own.

### The __init__() Method for a Child Class

- When you define a child class, the parent class must be part of the current file and must appear before the child class in the file. The name of the parent class must be included in parentheses in the definition of a child class. The __init__() method for a child class needs help from its parent class. A child class inherits the attributes of its parent class, but it’s also free to define attributes of its own. When you add new attributes to an instance through __init__(), those attributes are stored only in the instance being created. When you want to use inheritance, you want the child class to inherit the attributes and methods from its parent class, but you also want to add new attributes and methods. To do this, you need to call the __init__() method from the parent class. This will initialize the attributes that were defined in the parent __init__() method and make them available in the child class.

```python
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """
        Initialize attributes to describe a car.
        Set default value for odometer reading.
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
```

- The parent class must be part of the current file and must appear before the child class in the file
- the super() function is a special function that helps Python make connections between the parent and child class. This line tells Python to call the __init__() method from Car, which gives an ElectricCar instance all the attributes of its parent class. The name super comes from a convention of calling the parent class a superclass and the child class a subclass.

### Dealing Attributes and Methods for the Child Class

- You can define new attributes and methods for the child class, and you can override attributes and methods from the parent class. When you override a method from the parent class, you’re effectively replacing the parent class’s method with a new method that performs the same action or a similar action in the child class.

```python
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """
        Initialize attributes to describe a car.
        Set default value for odometer reading.
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class ElectricCar(Car):

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
```

### Overriding methods from the parent class

- You can override any method from the parent class that doesn’t fit what you’re trying to model with the child class. To do this, you define a method in the child class with the same name as the method you want to override in the parent class. Python will disregard the parent class method and only pay attention to the method you define in the child class.

```python

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """
        Initialize attributes to describe a car.
        Set default value for odometer reading.
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class ElectricCar(Car):

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
```

### Instance as Attributes

- You can model real-world situations more accurately by writing classes that depend on other classes. When one class requires another to function properly, you can use instances of one class as attributes of another class. You’ll also see how to use classes as attributes in your own classes.

```python

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """
        Initialize attributes to describe a car.
        Set default value for odometer reading.
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery:

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```

- Note: Battery has an aggregation relationship with the ElectricCar class

