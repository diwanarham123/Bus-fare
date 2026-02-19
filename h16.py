class Vehicle:
    """Represents a generic vehicle with seating capacity."""
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        """Calculates the default fare for the vehicle."""
        return self.seating_capacity * 100

class Bus(Vehicle):
    """Represents a Bus, inheriting from Vehicle, with an added maintenance charge."""
    def __init__(self, seating_capacity):
        super().__init__(seating_capacity)

    def fare(self):
        """Calculates the total fare for the bus, including a 10% maintenance charge."""
        base_fare = super().fare()
        maintenance_charge = base_fare * 0.10
        total_fare = base_fare + maintenance_charge
        return total_fare

bus = Bus(50)

print(f"Total fare for the Bus: INR {bus.fare()}")

is_bus_subclass_vehicle = issubclass(Bus, Vehicle)
is_vehicle_subclass_bus = issubclass(Vehicle, Bus)
