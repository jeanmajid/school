def toHex(string):
    hexValues = []
    for l in string:
        hexValues.append(hex(ord(l)))
    return hexValues

print(toHex("ABBA"))