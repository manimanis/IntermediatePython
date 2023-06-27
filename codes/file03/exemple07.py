# file03/exemple07.py
def compter(start, end):
    i = start
    while i <= end:
        yield i
        i += 1

for i in compter(1, 10):
    print(i, end=", ")
print()
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,