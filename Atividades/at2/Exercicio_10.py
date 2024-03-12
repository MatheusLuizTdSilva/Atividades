print("Bem-vindo!! Checador de maioridade")

def check_idade(idade: int):
    if idade <= 0:
        print("Idade inválida, digite uma idade positiva")
        return

def check(idade: int):
    if idade > 18:
        print("Você é maior de 18 anos")
        return

    if idade == 18:
        print("Você tem 18 anos")
        return
    print("Você é menor de 18 anos")

idade = int(input("Insira sua idade: "))

check(idade)