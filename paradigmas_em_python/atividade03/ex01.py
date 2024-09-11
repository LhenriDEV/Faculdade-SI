'''
Crie uma classe Aluno que encapsule os dados de um aluno, como nome e notas, e forneça métodos para manipular essas informações.
Requisitos: 
- Crie a classe Aluno com atributos privados __nome, __nota1 e __nota2.
- Implemente métodos públicos para definir e acessar as notas e o nome.
'''

class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.__nome = nome
        self.__nota1 = nota1
        self.__nota2 = nota2
    
    def definir_nome(self, nome):
        self.__nome = nome

    def definir_nota1(self, nota1):
        self.__nota1 = nota1

    def definir_nota2(self, nota2):
        self.__nota2 = nota2
    
    def obter_nome(self):
        return self.__nome
    
    def obter_nota1(self):
        return self.__nota1
    
    def obter_nota2(self):
        return self.__nota2
    
    def calcular_media(self):
        return (self.__nota1 + self.__nota2) / 2
    
    def mostrar_informacoes(self):
        media = self.calcular_media()
        print(f'Aluno: {self.__nome}\nMédia: {media:.2f}')


aluno1 = Aluno('Luis', 8.5, 7.0)
aluno1.mostrar_informacoes()

aluno1.definir_nome('João')
aluno1.definir_nota1(9.0)
aluno1.definir_nota2(8.5)
aluno1.mostrar_informacoes()