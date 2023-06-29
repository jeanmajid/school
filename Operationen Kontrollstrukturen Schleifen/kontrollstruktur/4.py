def istTeilbar(zahl, teiler):
    if teiler == 0:
        return False
    elif zahl % teiler == 0:
        return True
    else:
        return False

zahl = int(input("Bitte geben Sie eine Ganzzahl ein: "))

for num in range(1, zahl):
    if istTeilbar(zahl, num):
        print(f"{zahl} ist durch {num} Teilbar")

