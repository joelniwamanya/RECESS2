class Vehicle:
    def __init__(self, reg_no, rental_price):
        self.reg_no = reg_no
        self.rental_price = rental_price

    def calculate_rental_cost(self, days):
        return self.rental_price * days

    def display_info(self):
        print(f"Registration Number: {self.reg_no}")
        print(f"Rental Price Per Day: {self.rental_price}")


class Car(Vehicle):
    def __init__(self, reg_no, rental_price, seating_capacity):
        super().__init__(reg_no, rental_price)
        self.seating_capacity = seating_capacity

    def display_info(self):
        print("CAR DETAILS")
        print(f"Registration Number: {self.reg_no}")
        print(f"Rental Price Per Day: {self.rental_price}")
        print(f"Seating Capacity: {self.seating_capacity}")


class Motorcycle(Vehicle):
    def __init__(self, reg_no, rental_price, engine_capacity):
        super().__init__(reg_no, rental_price)
        self.engine_capacity = engine_capacity

    def display_info(self):
        print("MOTORCYCLE DETAILS")
        print(f"Registration Number: {self.reg_no}")
        print(f"Rental Price Per Day: {self.rental_price}")
        print(f"Engine Capacity: {self.engine_capacity}cc")


car1 = Car("UBA123A", 50000, 5)
bike1 = Motorcycle("UBB456B", 30000, 150)

car1.display_info()
print("Rental Cost for 3 days:", car1.calculate_rental_cost(3))

print()

bike1.display_info()
print("Rental Cost for 3 days:", bike1.calculate_rental_cost(3))