# file02/exemple04.py
lst = [1, 2, 1, 7, 3, 3, 2, 7, 5]
lst1 = [lst[i] for i in range(len(lst)) if lst.index(lst[i]) == i]
print(lst1) # [1, 2, 7, 3, 5]

