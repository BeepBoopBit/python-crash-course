# Lists

- A list is a collection of items in a particular order.
- You can put anything you want into a list, and the items in your list don't have to be related in any particular way.
- It's a good idea to make the name of the lsit plural, such as `bicycles`, `motorcycles`, or `users`.
- In python, square bracket `[]` indicate a list, and individual elements in the list are separated by commas.

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
```

## Accessing Elements in a list

- To access an element in a list, write the name of the list followed by the index of the item enclosed in square brackets. `print(bicycles[0])`.

### Index Position start at 0, not 1

- Python consider the first item in a list to be at position 0, not position 1.
- This is true to most of the programming langauges, and the reason has to do with how the list oeprations are implemented at a lower level.
- Python hsa a special syntax for accessing the last element in a list. By asking for the item at index `-1`, Python always returns the last item in the list. `print(bicycles[-1])`.

## Changing, Adding, and Removing Elements

### Modifying Elements in a List

- You can change an element in a list by accessing the element you want to change and then assigning a new value to that element. `motorcycles[0] = 'ducati'`.

### Adding Elements to a list

- You can add elements to the end of a list by using the `append()` method. `motorcycles.append('ducati')`.

### Inserting Elements into a list

- You can add a new element at any position in your list by using the `insert()` method. `motorcycles.insert(0, 'ducati')`.

### Removing Element's from a list

- You can remove an item using the `del` statement. `del motorcycles[0]`.

### Removing an Item using the pop() method

- The `pop()` method removes the last item in a list, but it lets you work with that item after removing it. `popped_motorcycle = motorcycles.pop()`.

### Popping items from any Position in a Lsit

- You can use the `pop()` method to remove an item in a list at any position by including the index of the item you want to remove in parentheses. `first_owned = motorcycles.pop(0)`.

### Removing an Item by Value

- You can remove an item by value if you don't know its position in the list. The `remove()` method deletes only the first occurrence of the value you specify. `motorcycles.remove('ducati')`.

### Sorting a List Permanently with the sort() method

- The `sort()` method changes the order of a list permanently. `cars.sort()`.

### Reverse sorting a list permanently

- You can reverse the original order of a list permanently with the `sort()` method. `cars.sort(reverse=True)`.

### Sorting a list Temporarily with sorted(0) function

- The `sorted()` function lets you display your list in a particular order but doesn't affect the actual order of the list. `print(sorted(cars))`.


### Sorting with both Uppercase and Lowercase

- Sorting a list alphabetically is a bit more complicated when all other values are not in lowercase. There are several ways to interpret capital letters when determining a sort order, and specifying the exact order can be more complex than we want to deal with at this time.

### Sorting in Reverse order

- You can reverse the original order of a list with the `reverse()` method. `cars.reverse()`.

### Finding the length of a list

- You can quickly find the length of a list by using the `len()` function. `len(cars)`.


### Summary of Methods use in Lists

- **append()** - Adds an item to the end of a list
- **insert()** - Adds an item at a specific position in a list
- **pop()** - Removes an item from a specific position in a list
- **remove()** - Removes an item by value
- **sort()** - Sorts items in a list permanently
- **sort(reverse=true)** - Sorts items in reverse order permanently
- **reverse()** - Reverses the order of a list permanently

## Others

- **[]** - Square brackets indicate a list, and individual elements in the list are separated by commas.
- **del** - Deletes an item from a list