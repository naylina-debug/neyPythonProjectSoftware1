numbers = []

while True:
    user_input = input("Enter a number (press Enter to quit): ")

    if user_input == "":
        break

    numbers.append(float(user_input))

if numbers:
    print("Smallest number:", min(numbers))
    print("Largest number:", max(numbers))
else:
    print("No numbers were entered.")

