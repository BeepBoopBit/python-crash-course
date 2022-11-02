class User:
    def __init__(self, fname, lname, *others):
        self.first_name = fname
        self.last_name = lname
        self.other = others[:]
    
    def describe_user(self):
        print(f"{self.first_name} {self.last_name}")
        print("Other Informations:")
        for i in self.other:
            print(f"- {i}")
    
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Privileges:")
        for i in self.privileges:
            print(f"- {i}")

class Admin(User):
    def __init__(self, fname, lname, *others):
        super().__init__(fname, lname, others)
        self.privileges = Privileges();
        
    def show_privileges(self):
        self.privileges.show_privileges()