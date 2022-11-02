import json
user_input = input("What is your favorite number: ")
json.dump(user_input, open("favorite_number.json", "w"))
