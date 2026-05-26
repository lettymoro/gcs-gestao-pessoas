pessoas = []

def cadastrar():
    nome = input("Digite o nome da pessoa: ")
    pessoas.append({"nome": nome})
    print("Pessoa cadastrada com sucesso!")

def menu():
    while True:
        print("\n--- Sistema de Gestão de Pessoas ---")
        print("1. Cadastrar pessoa")
        print("2. Listar pessoas")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar()
        elif opcao == '3':
            print("Encerrando...")
            break
        else:
            print("Funcionalidade em desenvolvimento...")

if __name__ == "__main__":
    menu()