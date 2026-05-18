from funcoes import *

def menu():
    escolha = 0

    while escolha != 9:
        print("1-Cadastrar novo jogador")
        print("2-Mostrar todos os jogadores cadastrados")
        print("3-Mostrar relatório completo")
        print("4-Pesquisar jogador pelo nome")
        print("5-Alterar informações de um jogador")
        print("6-Remover jogador do cadastro")
        print("7-Mostrar estatísticas gerais")
        print("8-Encerrar programa")
        
        escoha = int(input("\nDigite qual opção você quer: "))
