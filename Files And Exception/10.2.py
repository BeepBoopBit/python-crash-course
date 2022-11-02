message_list = []

with open("Files and Exception\learning_python.txt") as file_object:
    for line in file_object:
        line = line.replace("Python", "C")
        message_list.append(line)
    
print(message_list)