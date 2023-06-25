# file02/exemple07.py
counts = {chr(i+97): 0 for i in range(26)}
print(counts)

phrase = "Dictionary comprehension is a method for transforming one dictionary into another dictionary."
for car in phrase.lower():
    if car in counts:
        counts[car] += 1
print(counts)

counts = {key: value for key, value in counts.items() if value > 0}

mx, mn = max(counts.values()), min(counts.values())
max_counts = {key: value for key, value in counts.items() if value == mx or value == mn}
print(max_counts)

