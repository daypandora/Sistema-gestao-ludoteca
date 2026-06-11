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