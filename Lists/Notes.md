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
