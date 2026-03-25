import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_traveled = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.distance_traveled += self.current_speed * hours


class Race:
    def __init__(self, name, distance_km, car_list):
        self.name = name
        self.distance_km = distance_km
        self.cars = car_list

    def hour_passes(self):
        for vehicle in self.cars:
            speed_change = random.randint(-10, 15)
            vehicle.accelerate(speed_change)
            vehicle.drive(1)

    def print_status(self):
        print(f"\nRace: {self.name}")
        print(f"{'Car':<10} {'Speed (km/h)':<15} {'Distance (km)':<15}")
        print("-" * 40)
        for vehicle in self.cars:
            print(f"{vehicle.registration_number:<10} {vehicle.current_speed:<15} {vehicle.distance_traveled:<15}")

    def race_finished(self):
        for vehicle in self.cars:
            if vehicle.distance_traveled >= self.distance_km:
                return True
        return False

if __name__ == "__main__":
    cars = []

    for i in range(10):
        reg_number = f"ABC-{i+1}"
        car_max_speed = random.randint(100, 200)
        cars.append(Car(reg_number, car_max_speed))

    race = Race("Grand Demolition Derby", 8000, cars)

    total_hours = 0

    while not race.race_finished():
        total_hours += 1
        race.hour_passes()

        if total_hours % 10 == 0:
            print(f"\n--- Status after {total_hours} hours ---")
            race.print_status()

    print(f"\n Race finished in {total_hours} hours!")
    race.print_status()