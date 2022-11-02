
from random import randint
from sys import maxsize
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
die0 = Die()
die1 = Die()
die2 = Die()

for i in range(5000):
    rolls.append(die0.roll() + die1.roll() + die2.roll() )
    
max_size = die0.num_sides + die1.num_sides + die2.num_sides
frequency = [rolls.count(i) for i in range(2,max_size+1)]

x_value = [i for i in range(2,max_size+1)]
data = [Bar(x=x_value, y=frequency)]

my_layout = Layout(title="Rolls of Die 8", xaxis={'title':'data'}, yaxis={'title':'frequency'})
offline.plot({'data':data, 'layout':my_layout}, filename='d6.html')