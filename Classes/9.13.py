from random import randint

class Die:
    def __init__(self, sides = 6):
        self.sides = sides
    def roll_die(self):
        print(randint(1,self.sides))
        
        
sides = 6
for i in range(10):
    die = Die(sides)
    die.roll_die()
sides = 10
for i in range(10):
    die = Die(sides)
    die.roll_die()
sides = 20
for i in range(10):
    die = Die(sides)
    die.roll_die()