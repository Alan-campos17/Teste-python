usuarios = []

def cadastrar_usuario():
    nome = input("digite o nome:")
    idade = input("Digite sua idade:")
    email = input("Digite o seu email:")

    usuario = {
        "nome": nome,
        "idade": idade,
        "email": email
    }
usuarios.append(usuarios)
print("Usuario cadastrado cokm sucesso!.\n")

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuario cadastrado")
        return
    
    print("Lista de usuarios:")
    for i, u in enumerate(usuarios):
        print(f"(i + 1). Nome: {u('nome')}, Idade: {u('idade')}, Email: {u('Email')}")
        print()

def remover_usuario():
    listar_usuarios()
    if not usuarios:
        return
    try:
        indice = int(input({"Digite o numero do usuario que vc deseja remover"})) - 1
        if 0 <= indice <len(usuarios):
            removido = usuarios.pop(indice)
            print(f"Usuario'{removido['nome']}")
        else:
            print("opção Invalida")
    except ValueError:
        print("entrada inválida")
def menu():
    while True:
        print("==MENU==")
        print("1. Cadastrar Usuario")
        print("2. Listar usuarios")
        print("3. Remover Usuario")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao =="1":
            cadastrar_usuario()
        elif opcao =="2":
             listar_usuarios()
        elif opcao =="3":
            remover_usuario()
        elif opcao =="4":
            print("Encerrando o programa. Até mais")
            break
        else:
            print("opção Invalída. Tente novamente.\n")
menu()
