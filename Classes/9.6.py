class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
    
    def open_restaurant(self):
        print("The restaurant is open")
    
    def set_number_served(self, value):
        self.number_served = value
    
    def increment_number_served(self):
        self.number_served += 1


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors = ["vanilla", "chocolate", "strawberry"]):
        self.flavors = flavors
        super().__init__(restaurant_name, cuisine_type)
    
    def print_flavors(self):
        print(self.flavors)
    

ics = IceCreamStand("water", "melon");
ics.print_flavors();