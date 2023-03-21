lista_de_compras = []

while True:
    # Exibe as opções para o usuário
    print("Escolha uma opção:\n1 - Adicionar item\n2 - Remover item\n3 - Listar itens\n4 - Sair")
    opcao = input("Opção escolhida: ")

    if opcao == "1":
        # Adiciona um novo item à lista
        item = input("Digite o nome do item a ser adicionado: ")
        lista_de_compras.append(item)
        print(f"O item {item} foi adicionado à lista.")

    elif opcao == "2":
        # Remove um item da lista
        item = input("Digite o nome do item a ser removido: ")
        if item in lista_de_compras:
            lista_de_compras.remove(item)
            print(f"O item {item} foi removido da lista.")
        else:
            print(f"O item {item} não está na lista.")

    elif opcao == "3":
        # Exibe todos os itens da lista
        print("Itens na lista:")
        for item in lista_de_compras:
            print(item)

    elif opcao == "4":
        # Sai do programa
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")