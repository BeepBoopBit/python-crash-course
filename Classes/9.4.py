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
        
Restaurant1 = Restaurant("water", "melon");
Restaurant1.open_restaurant()
Restaurant1.describe_restaurant()
print(Restaurant1.number_served)
Restaurant1.number_served = 10
print(Restaurant1.number_served)
Restaurant1.set_number_served(20)
print(Restaurant1.number_served)
Restaurant1.increment_number_serve(20)
print(Restaurant1.number_served)
