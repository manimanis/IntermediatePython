def my_sum(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result

print(my_sum(5, 6, 7))