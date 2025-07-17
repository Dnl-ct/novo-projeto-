def menu():
    print("=== SISTEMA DE CADASTRO ===")
    print("1. Cadastrar pessoa")
    print("2. Listar cadastros")
    print("3. Buscar por nome")
    print("0. Sair")

cadastros = []

def cadastrar():
    nome = input("Nome: ")
    idade = input("Idade: ")
    cadastros.append({'nome': nome, 'idade': idade})
    print(f"{nome} cadastrado com sucesso!\n")

def listar():
    if not cadastros:
        print("Nenhum cadastro encontrado.\n")
    else:
        for c in cadastros:
            print(f"Nome: {c['nome']} - Idade: {c['idade']}")
        print()

def buscar():
    nome_busca = input("Digite o nome para buscar: ")
    encontrados = [c for c in cadastros if nome_busca.lower() in c['nome'].lower()]
    if encontrados:
        for c in encontrados:
            print(f"Nome: {c['nome']} - Idade: {c['idade']}")
    else:
        print("Nenhum cadastro encontrado com esse nome.")
    print()

while True:
    menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        buscar()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida.\n")