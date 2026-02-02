numbers = []

while True:
    user_input = input("Enter a number (empty to quit): ")

    if user_input == "":
        break

    numbers.append(float(user_input))

# Sort numbers in descending order
numbers.sort(reverse=True)

# Print the five greatest numbers
print("The five greatest numbers are:")
for number in numbers[:5]:
    print(number)
