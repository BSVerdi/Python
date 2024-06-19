def tabuleiro(posicoes):
    print()
    for i in range(0, 3):
            print(f' {posicoes[i][j]} ', end='')
            if j < 2:
                print('|', end='')
        if i < 2:
            print('\n---+---+---')
    print('\n')


def vencedor(jogador, posicoes):
    tabuleiro(posicoes)
    print(f'O jogador {jogador} venceu!')
    
    return False


posicoes = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
end = True
jogadas = 0

while end:
    tabuleiro(posicoes)
    if jogadas < 9:
        if jogadas % 2 == 0:
            jogador = 'X'
        else:
            jogador = 'O'
        while True:
            try:
                print(f'Vez do Jogador {jogador}')
                print('Escolha a posição: ')
                j, i = int(input('x = ')), int(input('y = '))
            except (TypeError, ValueError):
                print('Opção Inválida, tente novamente!')
            else:
                if posicoes[i][j] == ' ':
                    posicoes[i][j] = jogador
                    break
                else:
                    print('Opção Inválida, tente novamente!')
        if jogadas > 3:
            for c in range(0, 3):
                if posicoes[c][0] == posicoes[c][1] == posicoes[c][2] == jogador:
                    end = vencedor(jogador, posicoes)       
                elif posicoes[0][c] == posicoes[1][c] == posicoes[2][c] == jogador:
                    end = vencedor(jogador, posicoes)       
            if end:
                if posicoes[0][0] == posicoes[1][1] == posicoes[2][2] == jogador:
                    end = vencedor(jogador, posicoes)       
                elif posicoes[0][2] == posicoes[1][1] == posicoes[2][0] == jogador:
                    end = vencedor(jogador, posicoes)       
    else:
        print('Deu velha')
        end = False
    jogadas += 1
