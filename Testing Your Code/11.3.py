import unittest

class Employee():
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
    def give_raise(self, value = 5000):
        self.salary += value


class EmployeeTest(unittest.TestCase):
    def setUp(self):
        self.employees = [Employee('water','melon', 1000),
                          Employee('papaya', 'banana', 3000),
                          Employee('fruit', 'salad', 5000)]
    def test_give_custom_raise(self):
        for employee in self.employees:
            previousSalary = employee.salary
            employee.give_raise(200)
            self.assertEqual(employee.salary,previousSalary+200)
if __name__ == "__main__":
    unittest.main()