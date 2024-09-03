"""
Receber 4 notas pelo usuário e no final calcular a média final, se for maior ou igual a 7, aprovado, senão reprovado.
"""

def MostrarMedia(v1,v2,v3,v4):
    media = (v1+v2+v3+v4)/4
    if media >= 7:
        print(f"Sua média é {media} e você foi aprovado.")
    else:
        print(f"Sua média é {media} e você foi reprovado.")

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

MostrarMedia(n1,n2,n3,n4)