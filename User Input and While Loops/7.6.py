while True:
    user_input = int(input("Enter a your age: "))
    if user_input == 0:
        break;
    if user_input < 3:
        print("Your ticket is free")
    elif user_input < 12:
        print("Your ticket is $10")
    else:
        print("Your ticket is $15")