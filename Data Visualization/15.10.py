import matplotlib.pyplot as plt
from random import choice
from random import randint
import plotly.express as px
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

for i in range(5000):
    rolls.append(die0.roll() + die1.roll())
    
max_size = die0.num_sides + die1.num_sides
frequency = [rolls.count(i) for i in range(1,max_size+1)]

x_value = [i for i in range(1,max_size+1)]

fix, ax = plt.subplots()
ax.bar(x_value, frequency)
plt.show()

## RANDOM WALK

class RandomWalk:
    def __init__(self, num_points = 5000):
        self.num_points = num_points
        self.x = [0]
        self.y = [0]
    
    def get_step(self):
        value = choice([1,-1])
        direction = choice([0,1,2,3,4])
        return value * direction
    
    def fill_walk(self):
       while len(self.x) < self.num_points:
            x = self.get_step()
            y = self.get_step()
            
            # Reject moves that go nowhere
            if x == 0 and y == 0:
                continue
            
            self.x.append(self.x[-1] + x)
            self.y.append(self.y[-1] + y)

walk = RandomWalk()
walk.fill_walk()
fig = px.scatter(x=walk.x, y=walk.y)
offline.plot({'data': fig.data, 'layout': fig.layout}, filename='random_walk.html')
