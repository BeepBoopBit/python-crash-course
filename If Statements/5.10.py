current_users = ['water','melon','papaya','banana','fruit','salad']
new_users = ['stuff','eme', 'shemay', 'good', 'shit', 'bad', 'water']

for new in new_users:
    if new.upper() in current_users.upper():
        print("The username is already used")
    else:
        print("The username is available")