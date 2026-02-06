def get_second_largest(numbers):
    largest = 0
    second_largest = 0
    
    for number in numbers:
        if number > largest:
            second_largest = largest 
            largest = number
        elif number > second_largest:
                second_largest = number
    return second_largest
numbers = [19,5,13,15,7,6]
second_largest = get_second_largest(numbers)
print(f"second largest number is", second_largest)