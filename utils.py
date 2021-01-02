def find_max(list_numbers):
    max_number = 0
    for item in list_numbers:
        for number in list_numbers:
            if item > number and item > max_number:
                max_number = item

    return max_number
