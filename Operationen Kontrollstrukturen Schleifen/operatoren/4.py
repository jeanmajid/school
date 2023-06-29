num1 = float(input("Erste zahl: "))
num2 = float(input("Zweite zahl: "))

def modulus(num1, num2):
    return num1 - (num2 * (num1 // num2))


print(modulus(num1, num2))
