def remove_odd_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

# Main program
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cut_down_list = remove_odd_numbers(original_list)

print("Original list:", original_list)
print("List without odd numbers:", cut_down_list)
