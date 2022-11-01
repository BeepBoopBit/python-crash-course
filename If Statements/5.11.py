numbers = list(range(1,10))

for i in numbers:
    if i == 1:
        print(i + 'st')
    elif i == 2:
        print(i + 'nd')
    elif i == 3:
        print(i + 'rd')
    elif i == 4 or i == 5 or i == 6 or i == 7 or i == 8 or i == 9:
        print(i + 'th')
