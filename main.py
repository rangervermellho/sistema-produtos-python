from funcoes import *

produtos=carregar_produtos()

while True:
    print("\n=== SISTEMA DE PRODUTOS ===")
    print("\n1 - Cadastrar produto")
    print("2 - Mostrar produtos")
    print("3 - Produto mais caro")
    print("4 - Buscar produto")
    print("5 - Excluir produto")
    print("6 - Editar produto")
    print("7 - Sair")

    try:
        menu = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite apenas números.")
        continue

    if menu == 1:
        cadastrar_produto(produtos)
    elif menu == 2:
        mostrar_produtos(produtos)
    elif menu == 3:
        produto_mais_caro(produtos)
    elif menu == 4:
        buscar_produto_por_nome(produtos)
    elif menu == 5:
        excluir_produto_por_nome(produtos)
    elif menu == 6:
        editar_produto_por_nome(produtos)
    elif menu == 7:
        salvar_produtos(produtos)
        print("Salvando e saindo...")
        break
    else:
        print("Opção inválida.")