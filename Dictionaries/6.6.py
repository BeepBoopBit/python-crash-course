favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

people = ['jen', 'sarah', 'water', 'melon']
for i in people:
    if i in favorite_languages:
        print(f"{i}, Thank you for polling")
    else:
        print(i);