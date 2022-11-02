# Data Visualization

- Involves exploring data through visual representations.
- It's closely associated with data analysis, which uses cod to explore the patterns and connections in a data set.
- A data set can be made up of small list of numbers that fits in one line of code or it can be many gigabytes of data.

## Requirements

- Matplotlib
- python3
- Plotly

## Plotting a simple Line Graph

```python
import matplotlib.pyplot as plt
squares = [1,4,9,16,25]
fig,ax = plt.subplots()
ax.plot(squares)
plt.show()
```

- subplots() returns a tuple containing a figure and axes object(s). When we call plot() , we need to provide the set of values to plot and matplotlib plots the values in a list or tuple.
- The function can generate one or more plots in the same figure.
- `fig` represents the entire figure or collection of plots that are generated
- `ax` represents a single plot in the figure

## Changing the Label Type and Line Thickness

```python
import mathplotlib.pyplot as plt
square = [1,4,9,16,25]
fig,ax = plt.subplots()
ax.plot(square, linewidth=3)
# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
# Set size of tick labels
ax.tick_params(axis='both', labelsize=14)
```

- `ax.plot(square, linewidth=3)` sets the thickness of the line generated in the pllot
- `ax.set_title("Square Numbers", fontsize=24)` sets the title of the plot and the size of the font
- `ax.set_xlabel("Value", fontsize=14)` sets the label of the x-axis and the size of the font
- `ax.set_ylabel("Square of Value", fontsize=14)` sets the label of the y-axis and the size of the font
- `ax.tick_params(axis='both', labelsize=14)` sets the font size of the labels of both axis


## Correcting the Plot

- When you give plot() a sequence of numbers, it assumes the first data point corresponds to an x-coordinate value of 0, the second point corresponds to an x-coordinate value of 1, and so on.

```python
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.plot(input_values, squares, linewidth=5)

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)

# Show the plot
plt.show()
```

## Using Built-in styles

- MatPlotLib has a number of predefined styles available, with good starting settings for background colors, grid lines, line widths, fonts, font-sizes, and more that will make your plots look good with minimal effort.

```python 
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
square = [1, 4, 9, 16, 25]

plt.style.use("seaborn")
fig,ax = plt.subplots()

ax.plot(input_values, square, linewidth=3)

plt.show()
```

- `seaborn` is not supported anymore as of 3.6

## Plotting and Styling individual points with scatter()

- `scatter()` plots a single point for each set of x and y values that you provide. It's good for plotting a series of points and connecting them with lines.

```python
import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use("seaborn")
fig,ax = plt.subplots()

ax.scatter(x_values, y_values, s=100)

plt.show()
```

- `s` is used to set the size of the dots

## Calculating Data Automatically

```python
import matplotlib.pyplot as plt

x_values = range(1,1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')

fig,ax = plt.subplots()

# plot the points
ax.scatter(x_values, y_values, s=20)

# Set the range for each axis
ax.axis([0,1000,0,1000000])

plt.show()
```

## Defining Custom Colors

- To change the colors of the points, pass `c` to `scatter()` with the name of a color to use in quotation marks, as shown: `ax.scatter(x_values, y_values, c='red', s=10)`
- You can also define customer color as such: `ax.scatter(x_values,y_values,c=(0,0.8,0), s=10)`
  
## Using a Colormap

- A `colormap` is a series of color in a gradient that moves from a starting to an ending color. `ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)`
- You can see all the colormaps available in pyplot at https://matplotlib.org/; go to Examples, scroll down to Color, and click Colormap reference.

## Saving your plots automatically

```python
plt.savefig('name_of_the_figure.png', bbox_inches='tight')
```

## Random Walk

- A random walk is a path that has no clear direction but is determined by a series of random decisions, each of which is left entirely to chance. You can simulate a random walk with Python by choosing a direction and then calculating how far to go in that direction.

```python
from random import choice

class RandomWalk():
    """A class to generate random walks"""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk"""
        self.num_points = num_points

        # All walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk"""

        # Keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points:

            # Decide which direction to go and how far to go in that direction
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
```

### Generating Multiple Random Walks

```python
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active

while True:
    # Make a random walk, and plot the points
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Set the size of the plotting window
    plt.figure(dpi=128, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # Emphasize the first and last points
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Remove the axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
```

## Graphing with Plotly

```python
from random import randint
from turtle import title
from plotly.graph_objs import Bar, Layout
from plotly import offline

class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides
    def roll(self):
        return randint(1, self.num_sides)
    

# Setting-up the values
rolls = []
die = Die()
for i in range(1000):
    rolls.append(die.roll())

# Analyze the results.
frequencies = []
for i in range(1, die.num_sides+1):
    frequencies.append(rolls.count(i))
    
# Set up the x_values
x_values = list(range(1,die.num_sides+1))

# Create the Bar chart
data = [Bar(x=x_values, y=frequencies)]

# Set the title and labels
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

# Plot the chart
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
```

