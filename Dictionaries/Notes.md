# Dictionary

- Python dictionary is an unordered collection of items. While other compound data types have only value as an element, a dictionary has a key: value pair.

## A Simple Dictionary

```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
```

## Working with Dictionaries

- A dictionary in Python is a collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value associated with that key. A key’s value can be a number, a string, a list, or even another dictionary. In fact, you can use any object that you can create in Python as a value in a dictionary.
- In Python, a dictionary is wrapped in braces, {}, with a series of key-value pairs inside the braces, as shown in the following simple example:

```python
alien_0 = {'color': 'green', 'points': 5}
```

- A key-value pair is a set of values asscoiated with each other. When you provide a key, Python returns the value associated with that key.

## Accessing Values in a Dictionary

- To get the value associated with a key, give the name of the dictionary and then place the key inside a set of square brackets.

```python
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")
```

## Adding New Key-Value Pairs

- Dictionaries are dynamic structures, and you can add new key-value pairs to a dictionary at any time. You can also modify the value in a key-value pair any time you like.

```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
```

## Remove Key-Value Pairs

- You can remove key-value pairs from a dictionary if you no longer need the information that’s stored in it. The `del` statement completely removes a key-value pair. All del needs is the name of the dictionary and the key that you want to remove.

```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
```

## Using get() to Access values

- The `get()` method returns the value associated with a key if the key exists in the dictionary. If the key doesn’t exist, it returns the value of the second argument, or `None` if the second argument isn’t specified.

```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0.get('points'))
print(alien_0.get('speed', 'No speed value assigned.'))
```

## Looping Through a Dictionary

- You can loop through all the key-value pairs in a dictionary using a `for` loop. When looping through a dictionary, the key and value in each key-value pair are available inside the loop’s body.

```python
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
```

## Looping through all the keys in a dictionary

- If you’re interested in looping through all the keys in a dictionary, you can use the `keys()` method to return a list of all the keys in the dictionary.

```python
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key in user_0.keys():
    print(key.title())

# same as the top
for key in user_0:
    print(key.title())
```

## Looping through a dictionary’s keys in a particular order

- You can use the `sorted()` function to get a copy of the keys in order.

```python

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
```

## Looping Through all Values in a Dictionary

- If you’re interested in the values that a dictionary contains, you can use the `values()` method to return a list of values without any keys.

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
```

```python
for language in set(favorite_languages.values()):
    print(language.title())
```

- wrapping the values() method with the `set()` function removes any duplicate items from the list.

