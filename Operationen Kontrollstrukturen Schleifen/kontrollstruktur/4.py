def istTeilbar(zahl, teiler):
    if teiler == 0:
        return False
    elif zahl % teiler == 0:
        return True
    else:
        return False

zahl = int(input("Bitte geben Sie eine Ganzzahl ein: "))
teiler = []

for num in range(1, 1000000000000000000000000000):
    if istTeilbar(zahl, num):
        teiler.append(num)
        print(f"{zahl} ist durch {num} Teilbar")

