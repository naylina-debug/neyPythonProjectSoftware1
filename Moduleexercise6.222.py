import random

def roll_dice(sides):
    return random.randint(1, sides)

# Main program
max_number = int(input("Enter the number of sides on the dice: "))

roll = 0
while roll != max_number:
    roll = roll_dice(max_number)
    print(roll)
