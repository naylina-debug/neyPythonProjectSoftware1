class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor
        print(f"Elevator created. Starting at floor {self.current_floor}.")

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator moved up to floor {self.current_floor}")
        else:
            print("Already at the top floor.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator moved down to floor {self.current_floor}")
        else:
            print("Already at the bottom floor.")

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print("Target floor is out of range.")
            return

        print(f"Moving to floor {target_floor}...")
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
        print(f"Arrived at floor {self.current_floor}")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.num_elevators = num_elevators

        self.elevators = []
        for i in range(num_elevators):
            elevator = Elevator(bottom_floor, top_floor)
            self.elevators.append(elevator)

        print(f"Building created with {num_elevators} elevators.")

    def run_elevator(self, elevator_number, destination_floor):
        if elevator_number < 0 or elevator_number >= self.num_elevators:
            print("Invalid elevator number.")
            return

        print(f"\nRunning elevator {elevator_number} to floor {destination_floor}")
        self.elevators[elevator_number].go_to_floor(destination_floor)


# Main program (test)
if __name__ == "__main__":
    building = Building(1, 10, 3)  # 3 elevators, floors 1–10

    # Run some elevators
    building.run_elevator(0, 5)
    building.run_elevator(1, 8)
    building.run_elevator(2, 3)

    # Send them back to bottom floor
    building.run_elevator(0, 1)
    building.run_elevator(1, 1)
    building.run_elevator(2, 1)