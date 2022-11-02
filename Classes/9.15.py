from importlib.metadata import SelectableGroups
from random import randint

series_of_num = (1,2,3,4,5,6,7,8,9,10, 'a','b','c','d','e')

selected_values = []
user_values = [1,6,'a','c']

count = 0;
while user_values != selected_values:
    selected_values = []
    for i in range(4):
        selected_values.append(series_of_num[randint(0,14)])
    count += 1

probability = 1/count

print(f"The probability of you winning is: 1/{count} or {probability}")
