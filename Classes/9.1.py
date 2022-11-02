class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
    
    def open_restaurant(self):
        print("The restaurant is open")
        
Restaurant1 = Restaurant("water", "melon");
Restaurant1.open_restaurant()
Restaurant1.describe_restaurant()
