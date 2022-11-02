# Testing Your Codes

## Unit Testing and Test Cases

- Unit testing is a way to test your code to make sure it works as expected.
- The module *unittest* from the python standard library provides tools for testing your code.
- A *Unit test* verifies that one specific aspect of a function's behavior is correct.
- A *Test case* is a collection of unit tests that together prove that a function behaves as it's supposed to, within the full range of situations you expect it to handle.
  
## A Passing Test

- A passing test is a test that passes, that is, it doesn't cause an error and it doesn't fail an assertion test.

```python
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()
```

## A Failing Test

- A failing test is a test that fails, that is, it causes an error or it fails an assertion test.

```python
import unittest
class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
if __name__ == '__main__':
    unittest.main()
```

## Asset Methods

- The Table shows the most commonly used asset methods.

| Method | Checks that|
| --- | --- |
| assertEqual(a, b) | a == b |
| assertNotEqual(a, b) | a != b |
| assertTrue(x)  | bool(x) is True |
| assertFalse(x) | bool(x) is False |
| assertIn(item, list) | item in list |
| assertNotIn(item, list) | item not in list |

### The setUp() Method

- The *setUp()* method is a special method that Python runs automatically before each method starting with *test_*.

```python
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def setUp(self):
        """Create a full name and a formatted name."""
        self.first_name = 'janis'
        self.last_name = 'joplin'
        self.full_name = 'Janis Joplin'
        self.formatted_name = get_formatted_name(self.first_name, self.last_name)

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        self.assertEqual(self.formatted_name, self.full_name)

if __name__ == '__main__':
    unittest.main()
```

- When a test case is running. Python prints one character for each unit test as it is completed. A passing test prints a dot, a test that results in an error prints an E, and a test that results in a failed assertion prints an F. This is why you'll see a different number of dots and characters on the first line of output when you run your test cases. If a test case takes a long time to run because it contains many unit test, you can watch these results to get a sense of how many tests are passing.

