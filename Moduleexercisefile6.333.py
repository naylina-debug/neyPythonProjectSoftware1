def gallons_to_litres(gallons):
    return gallons * 3.78541

# Main program
gallons = float(input("Enter volume in gallons (negative value to stop): "))

while gallons >= 0:
    litres = gallons_to_litres(gallons)
    print(f"{gallons} gallons = {litres:.2f} litres")

    gallons = float(input("Enter volume in gallons (negative value to stop): "))
