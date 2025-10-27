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


if __name__ == "__main__":
    print("=== Cadastro de Funcionário ===")
    nome = input("Digite o nome do funcionário: ")
    cargo = input("Digite o cargo do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))

    funcionario = Funcionario(nome, cargo, salario)

    print("\n📋 Dados cadastrados:")
    print(funcionario.exibir_info())

    opcao = input("\nDeseja aplicar um aumento? (s/n): ")
    if opcao.lower() == "s":
        porcentagem = float(input("Digite a porcentagem de aumento: "))
        print(funcionario.aumentar_salario(porcentagem))
        print("\n📋 Dados atualizados:")
        print(funcionario.exibir_info())
