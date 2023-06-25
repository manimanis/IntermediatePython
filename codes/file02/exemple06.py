# file02/exemple06.py
phrase = "A set is a collection which is unordered and unindexed."
cars = {car for car in phrase.lower()}
print(cars)
# {'l', 'd', 'o', 'x', 'n', 'r', 'e', 'w', 's', 'i', 'u', '.', ' ', 'a', 'c', 'h', 't'}

alpha_cars = {chr(i + 97) for i in range(26) if chr(i + 97) not in cars}
print(alpha_cars)
# {'j', 'g', 'f', 'm', 'v', 'q', 'y', 'b', 'k', 'p', 'z'}

lettres = {chr(i + 97) for i in range(26)}
alpha_cars = lettres - cars
print(alpha_cars)