# Data Visualization

- Involves exploring data through visual representations.
- It's closely associated with data analysis, which uses cod to explore the patterns and connections in a data set.
- A data set can be made up of small list of numbers that fits in one line of code or it can be many gigabytes of data.

## Requirements

- Matplotlib
- python3

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

