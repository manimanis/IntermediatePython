def conv10(num_str, from_base=10):
    s = 0
    for dig in num_str:
        if "0" <= dig <= "9":
            v = ord(dig) - 48
        else:
            v = ord(dig) - 55
        s = s * from_base + v
    return s


# arguments positionnels
print(conv10("12"))  # 12 en base 10 --> 12
print(conv10("12", 8))  # 12 en base  8 --> 10
# arguments nommés
print(conv10(num_str="12"))  # 12 en base 10 --> 12
print(conv10(num_str="21", from_base=12))  # 12 en base 12 --> 25
print(conv10(from_base=5, num_str="12"))  # 12 en base 5  --> 7
# combinaison
print(conv10("12", from_base=8))  # 12 en base  8 --> 10
