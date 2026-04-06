import json
from produto import Produto


def cadastrar_produto(lista):   
    nome = input("Digite o nome do produto: ")
    try:
        valor = float(input("Digite o valor do produto: "))
    except ValueError:
        print("Valor inválido.")
        return
        
    produto = Produto(nome, valor)
    lista.append(produto)
    print("Produto cadastrado com sucesso!")


def mostrar_produtos(lista):
    if len(lista) == 0:
        print("Nenhum produto cadastrado.")
    else:
        print("Produtos cadastrados:")
    for p in lista:
        p.mostrar()


def produto_mais_caro(lista):
    if len(lista) == 0:
        print("Nenhum produto cadastrado.")
        return
        

    mais_caro = lista[0]

    for p in lista:
        if p.valor > mais_caro.valor:
            mais_caro = p

        print("Produto mais caro:")
        mais_caro.mostrar()


def buscar_produto_por_nome(lista):
    nome = input("Digite o nome do produto: ")

    for p in lista:
        if p.nome.lower() == nome.lower():
            print("Produto encontrado:")
            p.mostrar()
            return p

    print("Produto não encontrado!")
    return None


def excluir_produto_por_nome(lista):
    nome = input("Digite o nome do produto: ")

    for p in lista:
        if p.nome.lower() == nome.lower():
             lista.remove(p)
        print("Produto excluído!")
        return p

    print("Produto não encontrado!")
    return None


def editar_produto_por_nome(lista):
    nome = input("Digite o nome do produto: ")

    for p in lista:
        if p.nome.lower() == nome.lower():
            novo_nome = input("Novo nome: ")

            try:
                novo_valor = float(input("Novo valor: "))
            except ValueError:
                print("Valor inválido.")
                return

            p.nome = novo_nome
            p.valor = novo_valor
            print("Produto atualizado!")
            p.mostrar()
            return p

    print("Produto não encontrado!")


def salvar_produtos(lista):
    with open("produtos.json", "w", encoding="utf-8") as arquivo:
        json.dump([p.to_dict() for p in lista], arquivo, indent=4, ensure_ascii=False)


def carregar_produtos():
    try:
        with open("produtos.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        return [Produto.from_dict(p) for p in dados]
    except FileNotFoundError:
        return []