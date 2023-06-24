# file02/exemple03.py
phrase = "j'aime mon pays la TUNISIE"
nbv = 0
for car in phrase.lower():
    if car in "ouieya":
        nbv += 1
print(nbv)

nbv = len([car for car in phrase.lower() if car in "ouieya"])
print(nbv)

