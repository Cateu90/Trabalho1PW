import os
import time

def obter_opcao():
    os.system("cls")
    print("Cadastro de Produtos")
    print("-" * 20)
    print("1) Cadastrar Produto")
    print("2) Listar Produtos")
    print("3) Sair")
    return int(input("Opção desejada: "))

def validar_dados_produto(nome, preco, estoque) -> bool:
    if (type(nome) == str and
            type(preco) == float and
            type(estoque) == int)
        return True
    else:
        print("Dados inválidos. Tente novamente.")
        return False

   

def cadastrar_produto(produtos: dict):
    os.system("cls")
    print("Cadastrar Produto")
    print("-" * 17)
    codigo = len(produtos) + 1
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    estoque = int(input("Estoque: "))
    
    if validar_dados_produto(nome, preco, estoque):
        produtos[codigo] = (nome, preco, estoque)
        print("Produto cadastrado com sucesso!")
        time.sleep(2)
    else:
        print("Cadastro não realizado.")
        time.sleep(2)


def ler_dados_produto():
    os.system("cls")
    print("Cadastrar Produto")
    print("-" * 17)
    nome=input("Nome: ")
    preco = float(input("Preço: "))
    estoque = int(input("Estoque: "))
    return nome, preco, estoque

def persistir_dados_produto(produtos: dict, codigo: int):
def listar_produtos(produtos: dict):
    os.system("cls")
    print("Listar Produtos")
    print("-" * 40)
    print(f"Código {'Produto':<15} {'Preço':>10} {'Estoque':>10}")
    print("-" * 40)
    for codigo, (nome, preco, estoque) in produtos.items():
        print(f"{codigo :<06} {nome:<15} {preco:>10.2f} {estoque:>10d}")
    print("-" * 40)
    print("Pressione ENTER para voltar ao menu...", end="")
    input()
    print("Voltando ao menu...")
    time.sleep(2)

def main():
    produtos = {}
    while True:
        opcao = obter_opcao() 
        match opcao:
            case 1:
                cadastrar_produto(produtos)
            case 2:
                listar_produtos(produtos)
            case 3:
                print("Saindo do sistema...")
                time.sleep(2)
                os.system("cls")
                break  
            case _:
                print("Opção inválida. Voltando ao menu...")
                time.sleep(2)

if __name__ == "__main__":
    main()