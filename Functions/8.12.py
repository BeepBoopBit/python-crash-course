from venv import create


def create_sandwich(*toppings):
    print("Making a sandwich with the following toppings:")
    for topping in toppings:
        print("- " + topping)
create_sandwich("water","melon","papaya","banana")
    