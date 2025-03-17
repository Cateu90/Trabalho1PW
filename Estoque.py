import os
import time
from datetime import date
import json

estoque_txt = "estoque.txt"  

def obter_opcao() -> int:
    os.system("cls")
    print("Cadastro de Produtos")
    print("-" * 20)
    print("1) Cadastrar Produto")
    print("2) Listar Produtos")
    print("3) Sair")
    return int(input("Opção desejada: "))

def carregar_produtos():
    if not os.path.exists(estoque_txt):  
        return {}
    with open(estoque_txt, "r") as file:
        try:
            return json.load(file) or {}
        except json.JSONDecodeError:
            return {}
        
def salvar_produtos(produtos):
    with open(estoque_txt, "w") as file:
        json.dump(produtos, file, indent=4)

def cadastrar_produto(produtos: dict, codigo: int):
    nome, descricao, categoria, preco, estoque, perecivel = ler_dados_produto()
    persistir_dados_produto(produtos, codigo, nome, descricao, categoria, preco, estoque, perecivel)
    
def ler_dados_produto():
    os.system("cls")
    print("Cadastrar Produto")
    print("-" * 17)
    nome = ler_dado("Nome", str, validar_nome_produto)
    descricao = ler_dado("Descrição", str, validar_descricao_produto)
    categoria = ler_dado("Categoria", str, validar_categoria_produto)
    preco = ler_dado("Preço", float, validar_preco_produto)
    estoque = ler_dado("Estoque", int, validar_estoque_produto)
    perecivel = ler_dado("Perecível (0=Não, 1=Sim)", bool, validar_perecivel_produto)
    return nome, descricao, categoria, preco, estoque, perecivel

def validar_nome_produto(nome: str) -> bool:
    if len(nome) < 2:
        print("O nome do produto deve ter 2 ou mais caracteres. Tente novamente.")
        return False
    else:
        return True
    
def validar_descricao_produto(descricao: str) -> bool:
    if len(descricao) < 12:
        print("O descrição do produto deve ter 12 ou mais caracteres. Tente novamente.")
        return False
    else:
        return True

def validar_categoria_produto(categoria: str) -> bool:
    if len(categoria) < 4:
        print("A categoria do produto deve ter 4 ou mais caracteres. Tente novamente.")
        return False
    else:
        return True
    
def validar_preco_produto(preco: float) -> bool:
    if preco <= 0:
        print("O preço do produto deve ser maior que zero. Tente novamente.")
        return False
    else:
        return True
    
def validar_estoque_produto(estoque: int) -> bool:
    if estoque < 0:
        print("O estoque do produto deve ser maior ou igual a zero. Tente novamente.")
        return False
    else:
        return True

def validar_perecivel_produto(perecivel: bool) -> bool:
    return True

def tentar_converter(valor, tipo):
    try:
        if tipo == bool:
            if valor in ["0", "1"]:
                return bool(int(valor))
            else:
                return False
        valor_convertido = tipo(valor)
        return valor_convertido
    except ValueError:
        return False

def ler_dado(titulo, tipo, validar_atributo):
    while True:
        atributo = input(f"{titulo}: ")
        atributo = tentar_converter(atributo, tipo)
        if atributo is False and tipo != bool:
            print(f"{titulo} deve ser um valor válido. Tente novamente.")
            continue
        if not validar_atributo(atributo):
            continue
        return atributo    

def persistir_dados_produto(produtos, codigo, nome, descricao, categoria, preco, estoque, perecivel):
    produtos[str(codigo)] = [nome, descricao, categoria, preco, estoque, perecivel]  
    salvar_produtos(produtos)  
    print("Produto cadastrado com sucesso!")
    time.sleep(2)

def listar_produtos(produtos: dict):
    os.system("cls")
    print("Listar Produtos")
    print("-" * 47)
    print(f"Código {'Produto':15} {'Preço':>10} {'Estoque':>10}")
    print("-" * 47)
    for codigo, dados in produtos.items():
        nome, descricao, categoria, preco, estoque, perecivel = dados 
        print(f"{int(codigo):06d} {nome:15} {preco:>10.2f} {estoque:>10d}")
    print("-" * 47)
    print("Pressione ENTER para voltar ao menu...", end="")
    input()
    print("Voltando ao menu...")
    time.sleep(2)

def sair():
    print("Saindo do sistema...")
    time.sleep(2)
    os.system("cls")

def main():
    produtos = carregar_produtos()  
    codigo_produto = 1
    
   
    while True:
        opcao = obter_opcao()
        match opcao:
            case 1:
                cadastrar_produto(produtos, codigo_produto)
                codigo_produto += 1
            case 2:
                listar_produtos(produtos)
            case 3:
                sair()
                break
            case _:
                print("Opção inválida. Voltando ao menu...")
                time.sleep(2)

if __name__ == "__main__":
    main()