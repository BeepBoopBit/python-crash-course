from UserClass import User

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