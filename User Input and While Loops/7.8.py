sandwich_orders = ['water','melon','papaya','banana','fruit', 'salad']
finished_sandwiches = []

while sandwich_orders:
    finished_sandwiches.append(sandwich_orders.pop())
    print("I made your " + finished_sandwiches[-1] + " sandwich.")
    
