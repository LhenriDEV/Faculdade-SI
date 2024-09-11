"""
Exercício 2: Escopo Local e Global
Defina uma variável global chamada contador com o valor 0.
Crie uma função chamada incrementar_contador que incremente contador em 1 e imprima o valor atualizado.
Crie uma variável local dentro da função incrementar_contador chamada mensagem e defina-a como uma string.
Tente imprimir a variável mensagem fora da função e observe o que acontece.

"""

contador = 0 # Variável global

def incrementar_contador():
    global contador
    contador += 1
    print(contador)

    mensagem = "" # Variável local

print(mensagem) # Ocorrerá um erro pois esta variável está fora da função em que ela foi definida.