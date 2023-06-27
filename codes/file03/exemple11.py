# file03/exemple11.py
def contient(num, start=0):
    i = start
    while True:
        if str(num) in str(i):
            yield i
        i += 1

seq1 = contient(8, 90)
for i in range(3):
    print(next(seq1))
# 98, 108, 118

seq = contient(13, 200)
count = 0
while count < 5:
    val = next(seq)
    if val % 2 == 0:
        print(val)
        count += 1
