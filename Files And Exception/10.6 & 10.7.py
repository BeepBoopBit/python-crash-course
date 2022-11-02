user_input = input("Enter a number: ")
try:
    things = int(user_input)
    print("Thanks for following the instruction")
except ValueError:
    print("Why are you such a brat!!!?")
    print("JONKS HHAHAHAHAHAHA")
else:
    user_input = input("Enter another number: ")    
    try:
        user_input = int(user_input)
        print(things + user_input)
    except ValueError:
        print("Ok... now I'm not joking")
        print("Just kidding HAHHAHAHA")