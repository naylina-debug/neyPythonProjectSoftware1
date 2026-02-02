def sum_of_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# Main program
my_list = [3, 7, 2, 10, 5]
result = sum_of_list(my_list)
print("The sum of the list is:", result)
