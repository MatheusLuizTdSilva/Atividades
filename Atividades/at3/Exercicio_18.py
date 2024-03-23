num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

soma = num1 + num2 + num3

if soma > 0:
    print("A soma dos números é positiva.")
elif soma < 0:
    print("A soma dos números é negativa.")
else:
    print("A soma dos números é igual a zero.")