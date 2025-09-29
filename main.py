from todas_funcoes import *


def main():
    tabuleiro = [[0, -1,  0, -1,  0, -1,  0, -1],
                 [-1,  0, -1,  0, -1,  0, -1,  0],
                 [0, -1,  0, -1,  0, -1,  0, -1],
                 [0,  0,  0,  0,  0,  0,  0,  0],
                 [0,  0,  0,  0,  0,  0,  0,  0],
                 [1,  0,  1,  0,  1,  0,  1,  0],
                 [0,  1,  0,  1,  0,  1,  0,  1],
                 [1,  0,  1,  0,  1,  0,  1,  0]]

    colunas = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
    linhas = {'8': 0, '7': 1, '6': 2, '5': 3, '4': 4, '3': 5, '2': 6, '1': 7}

    jogador = 1

    fim_de_jogo = False

    while not fim_de_jogo:
        print(f'        Vez do Jogador {2 if jogador == -1 else 1}!\n')

        printa_tab(tabuleiro)

        total_pecas = contar_pecas(tabuleiro)
        teve_captura = False

        inicio = input('Selecione a peça que deseja mover: ').upper()

        if inicio == 'DESISTO':
            fim_de_jogo = True
            print(f'Fim de Jogo! O Jogador {2 if jogador == 1 else 1} venceu!')

        if len(inicio) != 2:
            print('Entrada inválida! Tente Novamente!')
            continue

        if not inicio[0] in linhas.keys() or not inicio[1] in colunas.keys():
            print('As coordenadas que você forneceu são inválidas! Tente Novamente')
            continue

        origem = linhas[inicio[0]], colunas[inicio[1]]
        movimentos_válidos = move(tabuleiro, jogador, origem)

        novo_tab = copia_tabuleiro(tabuleiro)
        for i in range(len(movimentos_válidos)):
            for j in range(len(movimentos_válidos[i])):
                if movimentos_válidos[i][j] == 1:
                    novo_tab[i][j] = 3

        print('Para essa peça, você pode realizar esses movimentos:\n')

        printa_tab(novo_tab)

        fim = input('Selecione a casa que deseja mover sua peça: ').upper()

        if len(fim) != 2:
            print('Entrada inválida! Tente Novamente!')
            continue

        if not fim[0] in linhas.keys() or not fim[1] in colunas.keys():
            print('As coordenadas que você forneceu são inválidas! Tente Novamente\n')
            continue

        destino = linhas[fim[0]], colunas[fim[1]]

        if movimentos_válidos[destino[0]][destino[1]] == 1:
            efetua_jogada(tabuleiro, origem, destino)

        else:
            print('Jogada Inválida! Tente novamente!\n')
            continue

        if total_pecas > contar_pecas(tabuleiro):
            teve_captura = True

        while True:
            if teve_captura:
                origem_temporaria = destino
                if existem_capturas_da_posicao(tabuleiro, jogador, origem_temporaria):
                    print(
                        'Você ainda tem captura(s)! Porém, para essa(s) você precisa apenas informar para onde quer mover a peça.')

                    movimentos_válidos = move(
                        tabuleiro, jogador, origem_temporaria)

                    novo_tab = copia_tabuleiro(tabuleiro)
                    for i in range(len(movimentos_válidos)):
                        for j in range(len(movimentos_válidos[i])):
                            if movimentos_válidos[i][j] == 1:
                                novo_tab[i][j] = 3

                    print('Para essa peça, você pode realizar esses movimentos:')

                    printa_tab(novo_tab)

                    destino_captura = input(
                        'Selecione para onde quer mover a peça: ').upper()

                    if len(destino_captura) != 2:
                        print('Entrada inválida! Tente Novamente!')
                        continue

                    if not destino_captura[0] in linhas.keys() or not destino_captura[1] in colunas.keys():
                        print(
                            'As coordenadas que você forneceu são inválidas! Tente Novamente')
                        continue

                    destino = linhas[destino_captura[0]
                                     ], colunas[destino_captura[1]]

                    if movimentos_válidos[destino[0]][destino[1]] == 1:
                        efetua_jogada(tabuleiro, origem_temporaria, destino)

                        cont = 0
                        for elem in tabuleiro:
                            for num in elem:
                                if num * jogador > 0:
                                    cont += 1
                        if cont == 0:
                            print(
                                f'Fim de Jogo! O Jogador {2 if jogador == 1 else 1} venceu!')

                            fim_de_jogo = True

                        jogador *= -1

                        cont = 0
                        for elem in tabuleiro:
                            for num in elem:
                                if num * jogador > 0:
                                    cont += 1
                        if cont == 0:
                            print(
                                f'Fim de Jogo! O Jogador {2 if jogador == 1 else 1} venceu!')
                            fim_de_jogo = True

                        jogador *= -1

                else:
                    break
            else:
                break


main()
