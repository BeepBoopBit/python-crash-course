username = input("What is your name: ")

with open("Files and Exception\guest.txt", "w") as file_object:
    file_object.write(username)
    