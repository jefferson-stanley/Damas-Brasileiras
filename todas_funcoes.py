def copia_tabuleiro(tab):
    novo_tabuleiro = []

    for linha_original in tab:
        nova_linha = []

        for item in linha_original:
            nova_linha.append(item)

        novo_tabuleiro.append(nova_linha)

    return novo_tabuleiro


def printa_tab(tabuleiro):
    num_linhas = len(tabuleiro)

    for i in range(len(tabuleiro)):
        linha = tabuleiro[i]

        print(num_linhas, end='   ')

        for j in range(len(linha)):
            peca = linha[j]

            cor_peca = 37
            if peca < 0:
                cor_peca = 30

            caractere = ' '

            if abs(peca) == 1:
                caractere = '●'
            if abs(peca) == 2:
                caractere = 'O'
            if peca == 3:
                caractere = '*'
                cor_peca = 31

            if i % 2 == 0:
                if j % 2 == 0:
                    if j <= len(linha) - 2:
                        print(f'\033[{cor_peca};47m{caractere:^3}', end='')

                if not j % 2 == 0:
                    if j <= len(linha) - 2:
                        print(f'\033[{cor_peca};40m{caractere:^3}', end='')
                    else:
                        print(f'\033[{cor_peca};40m {caractere}', '\033[0m')

            if not i % 2 == 0:
                if not j % 2 == 0:
                    if j <= len(linha) - 2:
                        print(f'\033[{cor_peca};47m{caractere:^3}', end='')
                    else:
                        print(f'\033[{cor_peca};47m {caractere}', '\033[0m')

                if j % 2 == 0:
                    if j <= len(linha) - 2:
                        print(f'\033[{cor_peca};40m{caractere:^3}', end='')

        num_linhas -= 1

    print('     A  B  C  D  E  F  G  H\n')


def efetua_jogada(tabuleiro, origem, destino):
    """Move a peça de origem para destino, captura se necessário e promove"""
    i, j = origem
    x, y = destino
    peca = tabuleiro[i][j]
    tabuleiro[i][j] = 0
    tabuleiro[x][y] = peca

    # Captura (peão)
    # Se tiver captura de peão, a aresta recebe 0

    if abs(peca) == 1 and abs(i - x) == 2:
        x_aresta = (i + x) // 2
        y_aresta = (j + y) // 2
        tabuleiro[x_aresta][y_aresta] = 0

        teve_captura = True

    # Captura (dama)
    if abs(peca) == 2 and abs(i - x) > 1:
        dx = (x - i) // abs(x - i)
        dy = (y - j) // abs(y - j)
        a, b = i + dx, j + dy

        while a != x and b != y:
            if tabuleiro[a][b] != 0:
                tabuleiro[a][b] = 0
                break

            a += dx
            b += dy

            teve_captura = True

    # Promoção
    if peca == 1 and x == 0:
        tabuleiro[x][y] = 2

    if peca == -1 and x == len(tabuleiro) - 1:
        tabuleiro[x][y] = -2


def existem_capturas_da_posicao(tabuleiro, jogador, origem):
    """
    Verifica se existe PELO MENOS UMA captura possível a partir de
    uma posição de origem específica. Retorna True ou False.
    """
    # 1. Desempacota as coordenadas de origem para usá-las.
    i, j = origem

    # 2. Pega a peça que está na casa de origem.
    peca = tabuleiro[i][j]

    # 3. Validação inicial: se a casa está vazia ou a peça não é do jogador,
    #    então com certeza não há capturas a partir daqui.
    if peca * jogador <= 0:
        return False

    n = len(tabuleiro)
    direcoes = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    # --- LÓGICA PARA PEÃO ---
    # Esta lógica é a mesma que a sua, mas sem os laços externos.
    if abs(peca) == 1:
        for dx, dy in direcoes:
            x_aresta, y_aresta = i + dx, j + dy
            x_pouso, y_pouso = i + 2*dx, j + 2*dy

            if 0 <= x_pouso < n and 0 <= y_pouso < n:
                peca_inimiga = tabuleiro[x_aresta][y_aresta]
                casa_de_pouso = tabuleiro[x_pouso][y_pouso]

                # Se encontrar uma única captura, retorna True.
                if peca_inimiga * jogador < 0 and casa_de_pouso == 0:
                    return True
                    
    elif abs(peca) == 2:
        for dx, dy in direcoes:
            encontrou_inimigo = False
            
            for k in range(1, n):
                x_passo = i + k * dx
                y_passo = j + k * dy

                if not (0 <= x_passo < n and 0 <= y_passo < n):
                    break  

                peca_no_caminho = tabuleiro[x_passo][y_passo]

                if encontrou_inimigo:
                    
                    if peca_no_caminho == 0:
                        return True  
                    else:
                        break  
                else:
                    if peca_no_caminho * jogador > 0:  
                        break
                    elif peca_no_caminho * jogador < 0:  
                        encontrou_inimigo = True
                        
    return False


def captura(tabuleiro, pos, dx, dy):
    """Verifica se a captura é possível a partir de pos na direção dx,dy"""
    n = len(tabuleiro)
    x = pos[0] + 2 * dx
    y = pos[1] + 2 * dy
    return 0 <= x < n and 0 <= y < n and tabuleiro[x][y] == 0


def move(tabuleiro, player, pos):
    n = len(tabuleiro)
    peca = tabuleiro[pos[0]][pos[1]]

    # Direções de movimento simples do peão (só pra frente)
    dir_move_peao = [(-1, -1), (-1, 1)] if player == 1 else [(1, -1), (1, 1)]
    # Direções de captura do peão (pra frente e pra trás)
    dir_captura_peao = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    # Direções da dama (todas)
    dir_dama = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    obrigatorias = []
    for i in range(n):
        for j in range(n):
            p = tabuleiro[i][j]
            if p * player > 0:
                if abs(p) == 1:  
                    for dx, dy in dir_captura_peao:
                        x1, y1 = i + dx, j + dy
                        x2, y2 = i + 2*dx, j + 2*dy
                        if 0 <= x2 < n and 0 <= y2 < n and 0 <= x1 < n and 0 <= y1 < n:
                            if tabuleiro[x1][y1] * player < 0 and tabuleiro[x2][y2] == 0:
                                obrigatorias.append((i, j))
                                break  
                else:  # dama
                    for dx, dy in dir_dama:
                        x, y = i + dx, j + dy
                        encontrou = False
                        while 0 <= x < n and 0 <= y < n:
                            if tabuleiro[x][y] == 0:
                                if encontrou:
                                    obrigatorias.append((i, j))
                                    break
                            elif tabuleiro[x][y] * player < 0:
                                if not encontrou:
                                    encontrou = True
                                else:
                                    break
                            else:
                                break
                            x += dx
                            y += dy

    moves = [[0]*n for _ in range(n)]

    if obrigatorias and pos not in obrigatorias:
        return moves

    if abs(peca) == 1:
        if not obrigatorias:
            for dx, dy in dir_move_peao:
                x, y = pos[0] + dx, pos[1] + dy
                if 0 <= x < n and 0 <= y < n and tabuleiro[x][y] == 0:
                    moves[x][y] = 1

        for dx, dy in dir_captura_peao:
            x1, y1 = pos[0] + dx, pos[1] + dy
            if 0 <= x1 < n and 0 <= y1 < n and tabuleiro[x1][y1] * player < 0:
                if captura(tabuleiro, pos, dx, dy):
                    moves[pos[0] + 2*dx][pos[1] + 2*dy] = 1

    else:
        for dx, dy in dir_dama:
            x, y = pos[0] + dx, pos[1] + dy
            encontrou = False
            while 0 <= x < n and 0 <= y < n:
                if tabuleiro[x][y] == 0:
                    if encontrou:
                        moves[x][y] = 1
                    elif not obrigatorias:
                        moves[x][y] = 1
                elif tabuleiro[x][y] * player < 0:
                    if not encontrou:
                        encontrou = True
                    else:
                        break
                else:
                    break
                x += dx
                y += dy

    return moves


def contar_pecas(tabuleiro):
    """Retorna a quantidade total de peças no tabuleiro (peões + damas de ambos os jogadores)."""
    count = 0

    for linha in tabuleiro:
        for casa in linha:
            if casa != 0:
                count += 1

    return count


def efetua_jogada(tabuleiro, origem, destino):
    """Move a peça de origem para destino, captura se necessário e promove"""
    i, j = origem
    x, y = destino
    peca = tabuleiro[i][j]
    tabuleiro[i][j] = 0
    tabuleiro[x][y] = peca

    if abs(peca) == 1 and abs(i - x) == 2:
        x_aresta = (i + x) // 2
        y_aresta = (j + y) // 2
        tabuleiro[x_aresta][y_aresta] = 0

    # Captura (dama)
    if abs(peca) == 2 and abs(i - x) > 1:
        dx = (x - i) // abs(x - i)
        dy = (y - j) // abs(y - j)
        a, b = i + dx, j + dy

        while a != x and b != y:
            if tabuleiro[a][b] != 0:
                tabuleiro[a][b] = 0
                break

            a += dx
            b += dy

    # Promoção
    if peca == 1 and x == 0:
        tabuleiro[x][y] = 2

    if peca == -1 and x == len(tabuleiro) - 1:
        tabuleiro[x][y] = -2
