nota_prova1 = float(input("Digite a nota da primeira prova: "))
nota_prova2 = float(input("Digite a nota da segunda prova: "))

media = (nota_prova1 + nota_prova2) / 2

if media >= 6:
    print("O aluno foi aprovado. Média:", media)
else:
    print("O aluno foi reprovado. Média:", media)