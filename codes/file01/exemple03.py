def my_sum(*args):
    result = 0
    for v in args:
        result += v
    return result

print(my_sum(5, 6, 7))