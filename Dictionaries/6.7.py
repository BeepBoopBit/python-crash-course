person0 = {
    'first_name': 'Renz',
    'last_name': 'Aguirre',
    'age': 18,
    'country': 'Philippines'
}
person1 = {
    'first_name': 'water',
    'last_name': 'melon',
    'age': 12,
    'country': 'Philippines'
}
person2 = {
    'first_name': 'papaya',
    'last_name': 'banana',
    'age': 13,
    'country': 'Philippines'
}

people = [person0, person1, person2]

for person in people:
    for k,v in person.items():
        print(f"{k}: {v}")
