def retorna_capturas(tabuleiro, jogador):
    """
    Verifica se o jogador tem ao menos uma captura obrigatória.
    tabuleiro: matriz NxN
    jogador: -1 (jogador 1) ou 1 (jogador 2)
    Peão = jogador
    Dama = jogador * 2
    """
    n = len(tabuleiro)
    direcoes = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    capturas = []

    for i in range(n):
        for j in range(n):
            peca = tabuleiro[i][j]
            jogada = []

            if peca == 0:
                continue

            # --------- PEÃO NORMAL ---------
            if peca == jogador:
                for dx, dy in direcoes:
                    x_aresta, y_aresta = i + dx, j + dy
                    x_pouso, y_pouso = i + 2*dx, j + 2*dy

                    if 0 <= x_pouso < n and 0 <= y_pouso < n:
                        if tabuleiro[x_aresta][y_aresta] != 0 and (tabuleiro[x_aresta][y_aresta] * jogador) < 0:
                            if tabuleiro[x_pouso][y_pouso] == 0:
                                jogada = [(i, j), (x_pouso, y_pouso)]
                                capturas.append(jogada)

            # --------- DAMA (COROADA) ---------
            if peca == jogador * 2:
                for dx, dy in direcoes:
                    x, y = i + dx, j + dy
                    encontrou_inimigo = False

                    while 0 <= x < n and 0 <= y < n:
                        if tabuleiro[x][y] == 0:
                            if encontrou_inimigo:
                                jogada = [(i, j), (x, y)]
                                capturas.append(jogada)
                        else:
                            if (tabuleiro[x][y] * jogador) > 0:
                                break  # encontrou peça amiga
                            if encontrou_inimigo:
                                break  # já tinha um inimigo, não pode ter dois seguidos
                            encontrou_inimigo = True

                        x += dx
                        y += dy

    return capturas


print(existe_captura(tabuleiro, 1))
