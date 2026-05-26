pessoas = []

def cadastrar():
    nome = input("Digite o nome da pessoa: ")
    pessoas.append({"nome": nome})
    print("Pessoa cadastrada com sucesso!")

def listar():
    if len(pessoas) == 0:
        print("Nenhuma pessoa cadastrada ainda.")
    else:
        print("\n--- Lista de Pessoas ---")
        for indice, pessoa in enumerate(pessoas):
            print(f"[{indice}] Nome: {pessoa['nome']}")

def buscar():
    termo = input("Digite o nome que deseja buscar: ")
    encontrado = False
    for indice, pessoa in enumerate(pessoas):
        if termo.lower() in pessoa['nome'].lower():
            print(f"Encontrado -> [{indice}] Nome: {pessoa['nome']}")
            encontrado = True
            
    if not encontrado:
        print("Ninguém encontrado com esse nome.")

def atualizar():
    listar()
    if len(pessoas) > 0:
        indice_str = input("Digite o número (entre colchetes) da pessoa que deseja atualizar: ")
        if indice_str.isdigit():
            indice = int(indice_str)
            if 0 <= indice < len(pessoas):
                novo_nome = input("Digite o novo nome: ")
                pessoas[indice]['nome'] = novo_nome
                print("Nome atualizado com sucesso!")
            else:
                print("Número não encontrado na lista.")
        else:
            print("Por favor, digite apenas números.")

def remover():
    listar()
    if len(pessoas) > 0:
        indice_str = input("Digite o número (entre colchetes) da pessoa que deseja remover: ")
        if indice_str.isdigit():
            indice = int(indice_str)
            if 0 <= indice < len(pessoas):
                removida = pessoas.pop(indice)
                print(f"A pessoa '{removida['nome']}' foi removida com sucesso!")
            else:
                print("Número não encontrado na lista.")
        else:
            print("Por favor, digite apenas números.")

def menu():
    while True:
        print("\n--- Sistema de Gestão de Pessoas ---")
        print("1. Cadastrar pessoa")
        print("2. Listar pessoas")
        print("3. Buscar pessoa")
        print("4. Atualizar pessoa")
        print("5. Remover pessoa")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar()
        elif opcao == '2':
            listar()
        elif opcao == '3':
            buscar()
        elif opcao == '4':
            atualizar()
        elif opcao == '5':
            remover()
        elif opcao == '6':
            print("Encerrando...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()