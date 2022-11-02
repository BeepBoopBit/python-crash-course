import matplotlib.pyplot as plt
from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import offline

class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides
    def roll(self):
        return randint(1, self.num_sides)
    

# Setting-up the values
rolls = []
die0 = Die()

for i in range(5000):
    rolls.append(die0.roll())
    
max_size = die0.num_sides
frequency = [rolls.count(i) for i in range(1,max_size+1)]

x_value = [i for i in range(2,max_size+1)]

fix, ax = plt.subplots()
ax.bar(x_value, frequency)
plt.show()


