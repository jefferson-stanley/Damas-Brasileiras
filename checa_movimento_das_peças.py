# checa_movimento das peças
def separa_l_col(entrada):
    linha, coluna = entrada.split()

    return linha, coluna


def eh_jogada_pedras(j, l_atual, col_atual, linha, coluna):
    eh_coluna = False
    eh_linha = False

    if coluna in range(1, 9) and coluna == col_atual - 1 or coluna == col_atual - 1:
        eh_coluna = True

    if j == 'j1':
        if linha in range(1, 9) and linha == l_atual + 1:
            eh_linha = True
    if j == 'j2':
        if linha in range(1, 9) and linha == l_atual - 1:
            eh_linha = True

    if eh_coluna and eh_linha:
        return True

    return False
