# Classe base (Empregado)
class Empregado:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base

# Subclasse Gerente
class Gerente(Empregado):
    def __init__(self, nome, salario_base, bonus_fixo):
        super().__init__(nome, salario_base)
        self.bonus_fixo = bonus_fixo

    def calcular_salario(self):
        return self.salario_base + self.bonus_fixo

class Vendedor(Empregado):
    def __init__(self, nome, salario_base, vendas, comissao):
        super().__init__(nome, salario_base)
        self.vendas = vendas
        self.comissao = comissao

    def calcular_salario(self):
        return self.salario_base + (self.vendas * self.comissao)


gerente = Gerente("Alice", 5000, 1000)
vendedor = Vendedor("Paulo", 3000, 20000, 0.05)


print(f"Salário total do Gerente {gerente.nome}: R$ {gerente.calcular_salario():.2f}")
print(f"Salário total do Vendedor {vendedor.nome}: R$ {vendedor.calcular_salario():.2f}")