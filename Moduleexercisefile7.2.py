# Create an empty set to store names
names = set()

while True:
    name = input("Enter a name (press Enter to stop): ")

    # Stop if the input is empty
    if name == "":
        break

    # Check if the name already exists
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

# Print all entered names
print("\nList of names:")
for n in names:
    print(n)
