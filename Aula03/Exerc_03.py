
def exibir_menu():
    print("\n=== Sistema de Usuários ===")
    print("1 - Cadastrar usuário")
    print("2 - Buscar usuário")
    print("3 - Remover usuário")
    print("4 - Listar todos usuários")
    print("5 - Sair")
    return input("Escolha uma opção: ")

# --- FUNÇÕES QUE ESTAVAM FALTANDO ---
def cadastrar_usuario(usuarios):
    nome = input("Nome do usuário: ").strip()
    if not nome:
        print("Nome não pode ser vazio.")
        return

    if nome in usuarios:
        print("Já existe um usuário com esse nome.")
        return

    email = input("E-mail (opcional): ").strip()
    idade = input("Idade (opcional): ").strip()

    usuarios[nome] = {"email": email, "idade": idade}
    print(f"Usuário '{nome}' cadastrado com sucesso!")

def buscar_usuario(usuarios):
    nome = input("Nome do usuário para buscar: ").strip()
    if nome in usuarios:
        dados = usuarios[nome]
        print(f"Encontrado: Nome: {nome}, Email: {dados.get('email','')}, Idade: {dados.get('idade','')}")
    else:
        print("Usuário não encontrado.")

def remover_usuario(usuarios):
    nome = input("Nome do usuário para remover: ").strip()
    if nome in usuarios:
        del usuarios[nome]
        print(f"Usuário '{nome}' removido com sucesso!")
    else:
        print("Usuário não encontrado.")
# --- FIM DAS FUNÇÕES QUE ESTAVAM FALTANDO ---

def processar_opcao(opcao, usuarios):
    if opcao == "1":
        cadastrar_usuario(usuarios)
    elif opcao == "2":
        buscar_usuario(usuarios)
    elif opcao == "3":
        remover_usuario(usuarios)
    elif opcao == "4":
        if usuarios:
            print("\n--- Usuários cadastrados ---")
            for nome, dados in usuarios.items():
                print(f"Nome: {nome}, Email: {dados.get('email','')}, Idade: {dados.get('idade','')}")
        else:
            print("\nNenhum usuário cadastrado.")
    else:
        print("Opção inválida!")

def main():
    # Banco de dados em memória
    usuarios = {}

    # Loop principal do programa
    while True:
        opcao = exibir_menu()

        if opcao == "5":
            print("Saindo do sistema...")
            break

        processar_opcao(opcao, usuarios)

if __name__ == "__main__":
    main()
