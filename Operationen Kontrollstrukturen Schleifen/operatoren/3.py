import math

kat1 = float(input("Erste kathete: "))
kat2 = float(input("Zweite kathete: "))

a = math.exp2(kat1)
b = math.exp2(kat2)
ergebnis = math.sqrt(a + b)

print(f"Deine Hypotenuse ist: {ergebnis}")