inches = float(input("Enter inches (negative number to stop): "))

while inches >= 0:
    centimeters = inches * 2.54
    print("Centimeters:", centimeters)

    inches = float(input("Enter inches (negative number to stop): "))

print("Program ended.")
