class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is now open!")

restaurant1 = Restaurant("Pasta Palace", "Italian")
restaurant2 = Restaurant("Sushi Central", "Japanese")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()

restaurant1.open_restaurant()
restaurant2.open_restaurant()