def get_string_length(str):
    count = 0
    for char in str:
        count += 1

    return count

str = "mahesh"
print("string length is", get_string_length(str))