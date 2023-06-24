# file02/exemple02.py
lst = []
for i in range(1, 11):
    if i % 2 == 1:
        lst.append(i)
print(lst) 
# [1, 3, 5, 7, 9]

lst = [i for i in range(1, 11) if i % 2 == 1]
print(lst) 
# [1, 3, 5, 7, 9]

lst = list(range(1, 11, 2))
print(lst) 
# [1, 3, 5, 7, 9]
