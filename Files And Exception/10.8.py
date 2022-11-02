
try:
    with open('Files And Exception\cats.txt', 'r') as file_object:
        print(file_object.read())
except FileNotFoundError:
    print("File not found")
else:
    try:
        with open('Files And Exception\dogs.txt', 'r') as file_object:
            print(file_object.read())
    except FileNotFoundError:
        print("File not found")