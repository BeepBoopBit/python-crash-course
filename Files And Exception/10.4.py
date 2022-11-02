while True:
    username = input("What is your name (q - quit): ")
    if username == 'q':
        break;
    with open("guest_book.txt", 'a') as file_object:
        file_object.write(username+ '\n')