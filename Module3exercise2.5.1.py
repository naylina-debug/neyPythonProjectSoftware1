# Medieval mass conversion program

# Constants
POUNDS_PER_TALENT = 20
LOTS_PER_POUND = 32
GRAMS_PER_LOT = 13.3

# User input
talents = int(input("Enter talents:\n"))
pounds = int(input("\nEnter pounds:\n"))
lots = float(input("\nEnter lots:\n"))

# Convert everything to lots
total_lots = (
        talents * POUNDS_PER_TALENT * LOTS_PER_POUND
        + pounds * LOTS_PER_POUND
        + lots
)

# Convert to grams
total_grams = total_lots * GRAMS_PER_LOT

# Convert to kilograms and grams
kilograms = int(total_grams // 1000)
grams = total_grams - kilograms * 1000

# Output
print("\nThe weight in modern units:")
print(f"{kilograms} kilograms and {grams:.2f} grams.")

