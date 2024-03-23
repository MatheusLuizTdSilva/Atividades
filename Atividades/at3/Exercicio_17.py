num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

soma = num1 + num2 + num3

if soma % 5 == 0:
    print("A soma dos números é divisível por 5.")
else:
    print("A soma dos números não é divisível por 5.")