def istTeilbar(zahl, teiler):
    if teiler == 0:
        return False
    elif zahl % teiler == 0:
        return True
    else:
        return False

zahl = int(input("Bitte geben Sie eine Ganzzahl ein: "))
teiler = int(input("Bitte geben Sie den Teiler ein: "))

if istTeilbar(zahl, teiler):
    print(zahl, "ist durch", teiler, "ohne Rest teilbar.")
else:
    print(zahl, "ist nicht durch", teiler, "ohne Rest teilbar.")
