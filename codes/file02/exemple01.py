# file02/exemple01.py
lst = []
for i in range(1, 11):
    lst.append(i*i)
print(lst) 
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

lst = [i*i for i in range(1, 11)]
print(lst) 
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]