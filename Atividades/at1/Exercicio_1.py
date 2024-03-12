def soma(valor1, valor2):
    return valor1 + valor2

def subtracao(valor1, valor2):
    return valor1 - valor2

def multicao(valor1, valor2):
    return valor1 * valor2

def divisao(valor1, valor2):
    if valor2 != 0: 
        return valor1 / valor2
    else:
        return "Não é possivel dividir por zero :( ."
    
print("Calculadora Matheus :) ")    

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

print("Escolha a opção desejada: ")
print("1. SOMA")
print("2. SUBTRAÇÃO")
print("3. MULTIPLIÇÃO")
print("4. DIVISÃO")

opcao = input("Digite o número da opção desejada: ")

if opcao == "1":
    print("Resultado: ", soma(valor1, valor2))
    
elif opcao == "2":
    print("Resultado: ", subtracao(valor1, valor2))
    
elif opcao == "3":
    print("Resultado: ", multicao(valor1, valor2))
    
elif opcao == "4":
    print("Resultado: ", divisao(valor1, valor2))
else:
    print("Opção invalida. Por favor, escolha uma opção válida.")
