while True:
    user_input = input("Why do you like programming (q - exit): ")
    if user_input == 'q':
        break;
    with open("Files and Exception\programming_poll.txt", 'a') as file_object:
        file_object.write(user_input+ '\n')
    