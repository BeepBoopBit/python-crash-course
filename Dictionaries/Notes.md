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


