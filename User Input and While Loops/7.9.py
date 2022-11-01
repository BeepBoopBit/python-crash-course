sandwich_orders = ['pastrami','water','pastrami','melon','papaya','pastrami','banana','fruit', 'salad']
finished_sandwiches = []

print("The deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    finished_sandwiches.append(sandwich_orders.pop())
    print("I made your " + finished_sandwiches[-1] + " sandwich.")
    
