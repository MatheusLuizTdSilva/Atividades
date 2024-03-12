print("Bem-Vindo a Calculadora de IMC de Matheus")

peso = float(input("Digite o peso desejado (Kg):"))
altura = float(input("Digite o altura desejado (Metros):"))

imc = peso / (altura * altura)

print(f"Seu IMC é:{imc:.2f}")