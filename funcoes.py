from listas import *

def calcularmedia(golsjogador, partidasjogador):

    if partidasjogador == 0:
        return 0

    return golsjogador / partidasjogador



def classificardesempenho(media):

    if media >= 2:
        return "Excelente"

    elif media >= 1:
        return "Bom"

    else:
        return "Precisa melhorar"



def cadastrar_jogador():

    continuar = "s" or "S"

    while continuar == "s" or "S":

        nome = input("Digite o nome do jogador: ")
        qtd_partidas = int(input("Digite a quantidade de partidas: "))
        qtd_gols = int(input("Digite a quantidade de gols/pontos: "))

        nomes.append(nome)
        partidas.append(qtd_partidas)
        gols.append(qtd_gols)

        print("Jogador cadastrado com sucesso.")

        continuar = input("Deseja cadastrar outro jogador? (s/n): ")



def mostrar_jogadores():

    if len(nomes) == 0:
        print("Nenhum jogador cadastrado.")

    else:
        print("\nLISTA DE JOGADORES")

        for i in range(len(nomes)):
            print(f"{nomes[i]}")



def mostrar_relatorio():

    if len(nomes) == 0:
        print("Nenhum jogador cadastrado.")

    else:
        print("\nRELATÓRIO DOS JOGADORES")

        for i in range(len(nomes)):

            media = calcularmedia(gols[i], partidas[i])
            desempenho = classificardesempenho(media)

            print(f"\nNome: {nomes[i]}")
            print(f"Partidas: {partidas[i]}")
            print(f"Gols/Pontos: {gols[i]}")
            print(f"Média por partida: {media:.2f}")
            print(f"Desempenho: {desempenho}")



def pesquisar_jogador():

    if len(nomes) == 0:
        print("Nenhum jogador cadastrado.")

    else:

        pesquisa = input("Digite o nome do jogador: ")

        if pesquisa in nomes:

            posicao = nomes.index(pesquisa)

            media = calcularmedia(gols[posicao], partidas[posicao])
            desempenho = classificardesempenho(media)

            print("\nDADOS DO JOGADOR")
            print(f"Nome: {nomes[posicao]}")
            print(f"Qt de partidas: {partidas[posicao]}")
            print(f"Gols ou Pontos: {gols[posicao]}")
            print(f"Média: {media:.2f}")
            print(f"Desempenho: {desempenho}")

        else:
            print("Jogador não encontrado.")


def alterar_jogador():

    if len(nomes) == 0:
        print("Nenhum jogador cadastrado.")

    else:

        jogador = input("Digite o nome do jogador: ")

        if jogador in nomes:

            posicao = nomes.index(jogador)

            novo_nome = input("Digite o novo nome: ")
            novas_partidas = int(input("Digite a nova quantidade de partidas: "))
            novos_gols = int(input("Digite a nova quantidade de gols/pontos: "))

            nomes[posicao] = novo_nome
            partidas[posicao] = novas_partidas
            gols[posicao] = novos_gols

            print("Dados alterados com sucesso.")

        else:
            print("Jogador não encontrado.")


def remover_jogador():

    if len(nomes) == 0:
        print("Nenhum jogador cadastrado.")

    else:

        jogador = input("Digite o nome do jogador: ")

        if jogador in nomes:

            posicao = nomes.index(jogador)

            nomes.pop(posicao)
            partidas.pop(posicao)
            gols.pop(posicao)

            print("Jogador removido com sucesso.")

        else:
            print("Jogador não encontrado.")


def mostrar_estatisticas():

    if len(nomes) == 0:
        print("Nenhum jogador cadastrado.")

    else:

        medias = []

        for i in range(len(nomes)):
            media = calcularmedia(gols[i], partidas[i])
            medias.append(media)

        maior_media = max(medias)
        menor_media = min(medias)
        media_geral = sum(medias) / len(medias)

        posicao_melhor = medias.index(maior_media)

        excelentes = 0
        precisam_melhorar = 0

        for media in medias:

            if media >= 2:
                excelentes += 1

            elif media < 1:
                precisam_melhorar += 1

        print("\nESTATÍSTICAS GERAIS")

        print(f"Quantidade total de jogadores: {len(nomes)}")
        print(f"Maior média de desempenho: {maior_media:.2f}")
        print(f"Menor média de desempenho: {menor_media:.2f}")
        print(f"Média geral dos jogadores: {media_geral:.2f}")
        print(f"Melhor jogador: {nomes[posicao_melhor]}")
        print(f"Quantidade de jogadores excelentes: {excelentes}")
        print(f"Quantidade de jogadores que precisam melhorar: {precisam_melhorar}")
