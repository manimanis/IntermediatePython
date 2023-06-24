# exemple11.py
mybox = ["cables", "headphones", "USB"]
item1, item2, item3 = mybox
print(item1, item2, item3)
# cables headphones USB

nbre = ["Nombres Premiers", 2, 3, 5, 7, 11, 13, 17, 19]
lib, *prems = nbre
print(lib)  # Nombres Premiers
print(prems)  # [2, 3, 5, 7, 11, 13, 17, 19]

savants = ["Newton", "Einstein", "Riemann"]
*physiciens, mathematicien = savants
print(physiciens)  # ['Newton', 'Einstein']
print(mathematicien)  # Riemann

ventes = [
    "Article",  # article
    1.5,  # prix unitaire
    20,
    25,
    13,
    16,
    37,  # dernières ventes
    0.19,  # TVA
    83,
]  # stock
art, pu, *qtes, tva, stock = ventes
print(art, pu, tva, stock)
print(qtes)
# Article 1.5 0.19 83
# [20, 25, 13, 16, 37]


l = [10, 20, 30, 40]
print(*l, sep="|")
# 10|20|30|40

l1 = [1, 3, 5, 7]
l2 = [3, 5, 7, 9]
l3 = [*l1, *l2]
print(l3)
# 2 4 6 3 5 7

s1 = {1, 3, 5, 7}
s2 = {3, 5, 7, 9}
s3 = {*s1, *s2}
print(s3)  # {1, 3, 5, 7, 9}


def somme4(a, b, c=0, d=0):
    return a + b + c + d

# liste de 2 éléments
l1 = [2, 4]
print(somme4(*l1)) # 6

# liste de 4 éléments
l1 = [1, 3, 5, 7]
print(somme4(*l1)) # 16
print(somme4(l1[0], l1[1], l1[2], l1[3])) # 16

