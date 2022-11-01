
dicts = []

while True:
    user_name = input("Give me your name: ")
    user_dream = input("Give me your dream place: ")
    dicts.append({user_name : user_dream})
    user_input = input("Do you want to continue? (y/n): ")
    if user_input == 'n':
        break;

for data in dicts:
    for k,v in data:
        print(k + " wants to go to " + v)
        
