import json
import os

jogos = [] #jogos cadastrados 
emprestimos = [] #emprestimos realizados

ARQUIVO = "ludoteca.json"

# Persistência dos dados

def carregar_dados():
    global jogos, emprestimos

    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            dados = json.load(f)
            jogos = dados.get("jogos", [])
            emprestimos = dados.get("emprestimos", [])
    else:
        jogos = []
        emprestimos = []

def salvar_dados():
    with open(ARQUIVO, "w") as f:
        json.dump({"jogos": jogos, "emprestimos": emprestimos}, f, indent=4)

# Menu de opções

def menu():
    print("\n===== SISTEMA DE GESTÃO DE LUDOTECA =====")
    print("1 - Adicionar jogo")
    print("2 - Remover jogo")
    print("3 - Listar jogos")
    print("4 - Buscar jogos por mecânica")
    print("5 - Buscar jogos por número de jogadores")
    print("6 - Emprestar")
    print("7 - Devolver")
    print("8 - Listar emprestados")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if 0 <= opcao <= 8:
        return opcao
    else:
        print("Opção inválida! Escolha uma opção entre 0 e 8.")
        return menu()
    
# Adicionar jogo

def adicionar_jogo():
    nome = input("Nome do jogo: ")
    mecanica = input("Mecânica: ")
    num_jogadores = int(input("Número de jogadores: "))

    jogo = {
        "nome": nome,
        "mecanica": mecanica,
        "num_jogadores": num_jogadores
    }

    jogos.append(jogo)
    salvar_dados()
    print(f"Jogo '{nome}' adicionado com sucesso!")

# Remover jogo

def remover_jogo():
    nome = input("Nome do jogo a remover: ")

    for jogo in jogos:
        if jogo["nome"].lower() == nome.lower():
            jogos.remove(jogo)
            salvar_dados()
            print(f"Jogo '{nome}' removido com sucesso!")
            return

    print(f"Jogo '{nome}' não encontrado!")

# Listar jogos

def listar_jogos():
    if not jogos:
        print("Nenhum jogo cadastrado!")
        return

    print("\nJogos cadastrados:")
    for jogo in jogos:
        print(f"- {jogo['nome']} (Mecânica: {jogo['mecanica']}, Jogadores: {jogo['num_jogadores']})")

# Buscar jogos por mecânica

def buscar_jogos_mecanica():
    mecanica = input("Mecânica a buscar: ")

    encontrou = False

    for jogo in jogos:
        if jogo["mecanica"].lower() == mecanica.lower():
            print(f"- {jogo['nome']} (Jogadores: {jogo['num_jogadores']})")
            encontrou = True

    if not encontrou:
        print(f"Nenhum jogo encontrado com a mecânica '{mecanica}'!")

# Buscar jogos por número de jogadores

def buscar_jogos_num_jogadores():
    num_jogadores = int(input("Número de jogadores a buscar: "))

    encontrou = False

    for jogo in jogos:
        if jogo["num_jogadores"] == num_jogadores:
            print(f"- {jogo['nome']} (Mecânica: {jogo['mecanica']})")
            encontrou = True

    if not encontrou:
        print(f"Nenhum jogo encontrado para {num_jogadores} jogadores!")

# Emprestar jogo

def emprestar_jogo():
    nome_jogo = input("Nome do jogo a emprestar: ")

    for jogo in jogos:
        if jogo["nome"].lower() == nome_jogo.lower():

            nome = input("Nome da pessoa: ")
            telefone = input("Telefone: ")
            endereco = input("Endereço: ")
            data_emprestimo = input("Data do empréstimo: ")

            emprestimo = {
                "nome": nome,
                "telefone": telefone,
                "endereco": endereco,
                "jogo": jogo["nome"],
                "data_emprestimo": data_emprestimo,
                "data_devolucao": "",
                "devolvido": False
            }

            emprestimos.append(emprestimo)
            salvar_dados()

            print(f"Jogo '{nome_jogo}' emprestado com sucesso!")
            return

    print(f"Jogo '{nome_jogo}' não encontrado!")

# Devolver jogo

def devolver_jogo():
    nome_jogo = input("Nome do jogo a devolver: ")

    for emprestimo in emprestimos:
        if emprestimo["jogo"].lower() == nome_jogo.lower() and not emprestimo["devolvido"]:
            data_devolucao = input("Data da devolução: ")
            emprestimo["data_devolucao"] = data_devolucao
            emprestimo["devolvido"] = True
            salvar_dados()
            print(f"Jogo '{nome_jogo}' devolvido com sucesso!")
            return

    print(f"Nenhum empréstimo encontrado para o jogo '{nome_jogo}'!")

# Listar emprestados 

def listar_emprestados():

    encontrou = False

    print("\n=== JOGOS EMPRESTADOS ===")

    for emprestimo in emprestimos:
        if not emprestimo["devolvido"]:
            print(
                f"- {emprestimo['jogo']} "
                f"(Emprestado para: {emprestimo['nome']}, "
                f"Data do empréstimo: {emprestimo['data_emprestimo']})"
            )
            encontrou = True

    if not encontrou:
        print("Nenhum jogo emprestado no momento!")

# Programa principal

carregar_dados()

opcao = menu()

while opcao != 0:
    if opcao == 1:
        adicionar_jogo()
    elif opcao == 2:
        remover_jogo()
    elif opcao == 3:
        listar_jogos()
    elif opcao == 4:
        buscar_jogos_mecanica()
    elif opcao == 5:
        buscar_jogos_num_jogadores()
    elif opcao == 6:
        emprestar_jogo()
    elif opcao == 7:
        devolver_jogo()
    elif opcao == 8:
        listar_emprestados()

    opcao = menu()

print("Sistema encerrado.")