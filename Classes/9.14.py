from random import randint

series_of_num = (1,2,3,4,5,6,7,8,9,10, 'a','b','c','d','e')

selected_values = []

for i in range(4):
    selected_values.append(series_of_num[randint(0,14)])

print(f"Any ticket matching these four numbers or letters wins a prize: {selected_values}")
