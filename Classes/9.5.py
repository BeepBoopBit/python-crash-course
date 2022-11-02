class User:
    def __init__(self, fname, lname, *others):
        self.first_name = fname
        self.last_name = lname
        self.other = others[:]
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"{self.first_name} {self.last_name}")
        print("Other Informations:")
        for i in self.other:
            print(f"- {i}")
    
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0

user00 = User("John", "D")
user01 = User("water", "melon", "fruit", "salad", "banana")
user02 = User("papaya", "banana", "fruit", "salad", "water", "melon")
user00.describe_user()
user01.describe_user()
user02.describe_user()

print(user00.login_attempts)
user00.increment_login_attempts()
print(user00.login_attempts)
user00.reset_login_attempts()
print(user00.login_attempts)
