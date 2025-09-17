# captura das peças
tabuleiro = [[0, 2, 0, 2, 0, 2, 0, 2]
             [2, 0, 2, 0, 2, 0, 2, 0]
             [0, 2, 0, 2, 0, 2, 0, 2]
             [0, 0, 0, 0, 0, 0, 0, 0]
             [0, 0, 0, 0, 0, 0, 0, 0]
             [1, 0, 1, 0, 1, 0, 1, 0]
             [0, 1, 0, 1, 0, 1, 0, 1]
             [0, 1, 0, 1, 0, 1, 0, 1]]


def captura_pedras(j, l_atual, col_atual, l_mov, col_mov):

    aresta1 = tabuleiro[l_atual - 1][col_atual - 1]
    aresta1_1 = tabuleiro[l_atual - 2][col_atual - 2]

    aresta2 = tabuleiro[l_atual - 1][col_atual + 1]
    aresta2_1 = tabuleiro[l_atual - 2][col_atual + 2]

    aresta3 = tabuleiro[l_atual + 1][col_atual - 1]
    aresta3_1 = tabuleiro[l_atual + 2][col_atual - 2]

    aresta4 = tabuleiro[l_atual + 1][col_atual + 1]
    aresta4_1 = tabuleiro[l_atual + 2][col_atual + 2]

    if aresta1 == 2 and aresta1_1 == 0 and l_mov == l_atual - 2 and col_mov == col_atual - 2:
        tabuleiro[l_atual - 1][col_atual - 1] = 0

        tabuleiro[l_atual][col_atual], tabuleiro[l_atual -
                                                 2][col_atual - 2] = 0, 1

    elif aresta2 == 2 and aresta2_1 == 0 and l_mov == l_atual - 2 and col_mov == col_atual + 2:
        tabuleiro[l_atual - 1][col_atual + 1] = 0

        tabuleiro[l_atual][col_atual], tabuleiro[l_atual -
                                                 2][col_atual + 2] = 0, 1

    elif aresta3 == 2 and aresta3_1 == 0 and l_mov == l_atual + 2 and col_mov == col_atual - 2:
        tabuleiro[l_atual + 1][col_atual - 1] = 0

        tabuleiro[l_atual][col_atual], tabuleiro[l_atual -
                                                 2][col_atual + 2] = 0, 1
