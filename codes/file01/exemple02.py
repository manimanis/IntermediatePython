def my_sum(my_ints):
    result = 0
    for v in my_ints:
        result += v
    return result

lints = [1, 2, 3]
print(my_sum(lints))