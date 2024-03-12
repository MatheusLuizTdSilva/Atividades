print("Bem vindo!!")

largura = float(input("Por favor dê um valor a largura: "))
comprimento = float(input("Por favor dê um valor ao comprimento: "))

area = largura * comprimento
peri = comprimento * 2 + largura * 2

print(f"e o perímetro é {peri:.2f} m²")
print(f"A área do retângulo é {area:.2f} m²")