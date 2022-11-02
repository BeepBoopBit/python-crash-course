import json
user_input = input("What is your favorite number: ")

data = "a"
with open("Files And Exception\\favorite_number.json") as f:
    data = json.load(f) 
    
if data == user_input:
    print(f"Welcome Back! {user_input}")
else:
    print("I'll remember you")
with open("Files And Exception\\favorite_number.json", "w") as f:
    json.dump(user_input, f)
    
