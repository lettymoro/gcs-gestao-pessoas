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

def menu():
    while True:
        print("\n--- Sistema de Gestão de Pessoas ---")
        print("1. Cadastrar pessoa")
        print("2. Listar pessoas")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar()
        elif opcao == '2':
            listar()
        elif opcao == '3':
            print("Encerrando...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()