from funcoes import *

opcao = 0

while opcao != 8:

    print("\nMENU")
    print("1 - Cadastrar novo jogador")
    print("2 - Mostrar todos os jogadores cadastrados")
    print("3 - Mostrar relatório completo")
    print("4 - Pesquisar jogador pelos nomes")
    print("5 - Alterar informações de jogadores")
    print("6 - Remover jogador dos cadastros")
    print("7 - Mostrar estatísticas gerais")
    print("8 - Fechar programa")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        cadastrar_jogador()

    elif opcao == 2:
        mostrar_jogadores()

    elif opcao == 3:
        mostrar_relatorio()

    elif opcao == 4:
        pesquisar_jogador()

    elif opcao == 5:
        alterar_jogador()

    elif opcao == 6:
        remover_jogador()

    elif opcao == 7:
        mostrar_estatisticas()

    elif opcao == 8:
        print("Programa encerrado.")

    else:
        print("Opção inválida.")
