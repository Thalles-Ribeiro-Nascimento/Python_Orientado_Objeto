class Vehicle:

    def __init__(self, name, max_speed, capacity):
        self.name = name
        self.max_speed = max_speed
        self.capacity = capacity
    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10  / 100
        return amount
School_bus = Bus("Volvo", 180, 50)
print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Km/h", "Mileage: US$", School_bus.fare(),)

