import random

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

cars = []
for i in range(1, 11):
    reg_number = f"ABC-{i}"
    max_speed = random.randint(100, 200)
    cars.append(Car(reg_number, max_speed))

race_finished = False
hours_passed = 0

while not race_finished:
    hours_passed += 1

    for car in cars:
        change = random.randint(-10, 15)
        car.accelerate(change)

        car.drive(1)

        if car.travelled_distance >= 10000:
            race_finished = True

print(f"{'Reg Number':<10} {'Max Speed':<10} {'Speed':<10} {'Distance':<10}")
print("-" * 45)

for car in cars:
    print(f"{car.registration_number:<10} {car.maximum_speed:<10} {car.current_speed:<10} {car.travelled_distance:<10.2f}")

print("\nTotal race hours:", hours_passed)