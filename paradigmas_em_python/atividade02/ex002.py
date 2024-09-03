"""
Criar um programa simples para determinar se um número é par ou ímpar
"""

def ParOuImpar(v1):
    resto = v1 % 2
    if resto == 0:
        print(f"O número {v1} é par.")
    else:
        print(f"O número {v1} é impar.")

n1 = int(input("Digite um número: "))
ParOuImpar(n1)