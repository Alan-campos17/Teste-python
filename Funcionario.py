class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def exibir_info(self):
        return f"Nome: {self.nome}, Cargo: {self.cargo}, Salário: R${self.salario:.2f}"

    def aumentar_salario(self, porcentagem):
        self.salario += self.salario * (porcentagem / 100)
        return f"Novo salário de {self.nome}: R${self.salario:.2f}"
