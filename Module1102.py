class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        new_speed = self.current_speed + speed_change
        if new_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity_kwh):
        super().__init__(registration_number, maximum_speed)
        self.battery_capacity_kwh = battery_capacity_kwh


class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank_volume_liters):
        super().__init__(registration_number, maximum_speed)
        self.tank_volume_liters = tank_volume_liters


if __name__ == "__main__":
    electric = ElectricCar("ABC-15", 180, 52.5)
    gasoline = GasolineCar("ACD-123", 165, 32.3)

    electric.accelerate(150)
    gasoline.accelerate(140)

    electric.drive(3)
    gasoline.drive(3)

    print(f"Electric car {electric.registration_number}:")
    print(f"  Travelled distance: {electric.travelled_distance:.1f} km")
    print()
    print(f"Gasoline car {gasoline.registration_number}:")
    print(f"  Travelled distance: {gasoline.travelled_distance:.1f} km")