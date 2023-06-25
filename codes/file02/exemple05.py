# file02/exemple05.py
from random import randint, seed

seed(2)
l1 = [(randint(1, 6), 
       randint(1, 6), 
       randint(1, 6)) for _ in range(6)]
print(l1)
# [(1, 1, 1), (3, 2, 6), (6, 3, 3), (5, 2, 5), (1, 5, 6), (2, 4, 6)]

s1 = {v1+v2+v3 for v1, v2, v3 in l1}
print(s1)
# {11, 3, 12}

s2 = {v for v in range(3, 19) if v not in s1}
print(s2)
# {4, 5, 6, 7, 8, 9, 10, 13, 14, 15, 16, 17, 18}