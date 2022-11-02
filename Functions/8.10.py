def show_message(message, newDir):
    while message:
        current = message.pop()
        print(current)
        newDir.append(current)
        
listA = ['water','melon','papaya', 'banana', 'fruit', 'salad']
sentMessages = []

show_message(listA, sentMessages)