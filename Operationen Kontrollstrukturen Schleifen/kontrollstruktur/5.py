import math

x = float(input("Bitte geben Sie die x-Wert an:"));
y = float(input("Bitte geben Sie die y-Wert an:"));

r = math.sqrt(x**2 + y**2)
o = math.degrees(math.atan2(y, x))

print("Der betrag r beträgt ", r)
print("Der Winkel o beträgt ", o)
