tabuleiro = [[0, 2, 0, 2, 0, 2, 0, 2],
             [2, 0, 2, 0, 2, 0, 2, 0],
             [0, 2, 0, 2, 0, 2, 0, 2],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [1, 0, 1, 0, 1, 0, 1, 0],
             [0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0]]

num_linhas = 8

print('     A  B  C  D  E  F  G  H\n')

for i in range(len(tabuleiro)):
    linha = tabuleiro[i]

    print(num_linhas, end='   ')

    for j in range(len(linha)):
        num = linha[j]

        caractere = '•'
        cor_peca = 37

        if num == 0:
            caractere = ' '
        if num == 2:
            cor_peca = 30


        if i % 2 == 0:
            if j % 2 == 0:
                if j <= len(linha) - 2:
                    print(f'\033[{cor_peca};47m {caractere} ', end='')

            if not j % 2 == 0:
                if j <= len(linha) - 2:
                    print(f'\033[{cor_peca};40m {caractere} ', end='')
                else:
                    print(f'\033[{cor_peca};40m {caractere}', '\033[0m')

        if not i % 2 == 0:
            if not j % 2 == 0:
                if j <= len(linha) - 2:
                    print(f'\033[{cor_peca};47m {caractere} ', end='')
                else:
                    print(f'\033[{cor_peca};47m {caractere}', '\033[0m')

            if j % 2 == 0:
                if j <= len(linha) - 2:
                    print(f'\033[{cor_peca};40m {caractere} ', end='')

    num_linhas -= 1

