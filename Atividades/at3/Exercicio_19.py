ano_nascimento = int(input("Digite o ano de nascimento: "))

ano_atual = 2023
idade = ano_atual - ano_nascimento

if idade >= 16:
    print("Você está apto(a) a votar!")
else:
    print("Você não está apto(a) a votar.")