# Medieval mass conversion program

# Constants
LOTS_PER_POUND = 32
POUNDS_PER_TALENT = 20
GRAMS_PER_LOT = 13.3

# User input
talents = int(input("Enter talents (leiviskä): "))
pounds = int(input("Enter pounds (naula): "))
lots = int(input("Enter lots (luoti): "))

# Convert everything to lots
total_lots = (
        talents * POUNDS_PER_TALENT * LOTS_PER_POUND
        + pounds * LOTS_PER_POUND
        + lots
)

# Convert lots to grams
total_grams = total_lots * GRAMS_PER_LOT

# Convert grams to kilograms and remaining grams
kilograms = int(total_grams // 1000)
grams = total_grams % 1000

# Output result
print(f"The mass is {kilograms} kilograms and {grams:.2f} grams.")

