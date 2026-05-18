from listas import *

def cadastrarAluno():

    continuar = 'S' or 's'

    while continuar == 'S' or 's':


        nome = input("Digite o nome do jogador: ")
        partidas = input("Digite a quantidade de partidas jogadas: ")
        gols = input("Digite a quantidade de gols: ")

        nomes.append(nome)
        quantidadePartidas.append(partidas)
        quantidadeGols.append(gols)

        print("Aluno cadastrado!")

        continuar = input("Deseja continuar cadastrando alunos?  (S/N): ")

def mostrar_alunos():
    print(nomes)
