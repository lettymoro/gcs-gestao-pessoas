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
        # Transforma tudo em letra minúscula para facilitar a busca
        if termo.lower() in pessoa['nome'].lower():
            print(f"Encontrado -> [{indice}] Nome: {pessoa['nome']}")
            encontrado = True
            
    if not encontrado:
        print("Ninguém encontrado com esse nome.")

def menu():
    while True:
        print("\n--- Sistema de Gestão de Pessoas ---")
        print("1. Cadastrar pessoa")
        print("2. Listar pessoas")
        print("3. Buscar pessoa")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar()
        elif opcao == '2':
            listar()
        elif opcao == '3':
            buscar()
        elif opcao == '4':
            print("Encerrando...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()