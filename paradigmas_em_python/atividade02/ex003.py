"""
Receber a quantidade de notas pelo usuário que será calculado e no final calcular a média final, se for maior ou igual a 7, aprovado senão
reprovado.

1. Receber do usuário quantas notas ele quer calcular
2. A partir dessa quantidade, eu vou calcular a média de acordo com as notas que ele me der
"""

QuantNotas = int(input("Digite a quantidade de notas que você deseja calcular: "))
SomaNotas = 0

for item in range(QuantNotas):
    nota = float(input(f"Digite a nota {item + 1}: "))
    SomaNotas += nota

media = SomaNotas / QuantNotas

if media >= 7:
    print(f"Sua média foi {media:.2f}. Parabéns, você foi aprovado!")
else:
    print(f"Sua média foi {media:.2f}. Infelizmente, você foi reprovado.")