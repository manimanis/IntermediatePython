# file03/exemple09.py
hexa = (hex(i)[2:] for i in range(16) if i % 2 == 0)
print(*hexa, sep=",")