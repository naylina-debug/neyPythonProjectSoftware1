# Size limit for a zander (in cm)
SIZE_LIMIT = 42

# Ask the fisher for the length of the fish
length = float(input("Enter the length of the zander (cm): "))

# Check if the fish meets the size limit
if length < SIZE_LIMIT:
    difference = SIZE_LIMIT - length
    print("The zander is too small.")
    print(f"Release the fish back into the lake.")
    print(f"It is {difference:.1f} cm below the size limit.")
else:
    print("The zander meets the size limit. You may keep the fish.")

