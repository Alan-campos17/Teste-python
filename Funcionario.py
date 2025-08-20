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


# Se o arquivo for executado diretamente, roda esse teste
if __name__ == "__main__":
    f1 = Funcionario("João", "Desenvolvedor", 3500)
    print("📋 Dados do Funcionário:")
    print(f1.exibir_info())

    print("\n💸 Aplicando aumento de 15%...")
    print(f1.aumentar_salario(15))

    print("\n📋 Dados atualizados:")
    print(f1.exibir_info())
