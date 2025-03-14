clientes = []

while True:
    print("\n ==Menu==")
    print("1. Cadastrar novo cliente")
    print("2. Listar  clientes cadastrados")
    print("3. sair")

    opcao = input("\n Escolha uma opção")

    if opcao == '1':
        print = ("\n Novo Cadastro")
        nome = input("Nome completo:")
        telefone = input("telefone:")

        clientes = {
            'nome': nome,
            'telefone': telefone
        }

        clientes.append(cliente)
        print("\n cliente cadastrado com sucesso")

    elif opcao == '2':
        print("\n--- clientes cadastrados---")
        if len(clientes) == 0:
            print("Nemhum cliente cadastrado")
        else:
            for i, cliente in enumerate(clientes, 1):
                print(f"\n cliente{i}:")
                print(f"Nome{cliente['nome']}")
                print(f"Telefone: {cliente['telefone']}")
    elif opcao == '3':
        print("\n Saindo do sistema...")
        break
    else:
        print("\n Opção inválida! Tente novamente.")