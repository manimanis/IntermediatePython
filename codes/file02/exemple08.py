# file02/exemple08.py
from random import choice, seed

seed(8912)

custs = ["Amine", "Helmi", "Sarra", "Hiba"]
discs = [choice([25, 50]) for _ in custs]

cust_disc = {cust: disc for cust, disc in zip(custs, discs)}
print(cust_disc)

h_count = {cust: disc for cust, disc in cust_disc.items() if cust.startswith('H')}
print(h_count) # {'Helmi': 25, 'Hiba': 25}

