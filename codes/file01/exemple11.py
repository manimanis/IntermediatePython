# exemple11.py
l = [10, 20, 30, 40]
print(*l, sep="|")
# 10|20|30|40

l2 = [2, 4, 6]
l3 = [3, 5, 7]
l4 = [*l2, *l3]
print(*l4)
# 2 4 6 3 5 7