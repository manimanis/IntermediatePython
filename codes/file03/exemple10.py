# file03/exemple10.py
def facteurs(n):
    f = 2
    end = int(n**.5)+1
    while f > 1:
        if n % f == 0:
            yield f
            n //= f
        elif f == 2:
            f = 3
        elif f <= end:
            f += 2
        else:
            f = n

for f in facteurs(2*3*3*5*13):
    print(f)
