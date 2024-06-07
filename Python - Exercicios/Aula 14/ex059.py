from time import sleep
d = 0
v1 = float(input('Insira o 1º valor: '))
v2 = float(input('Insira o 2º valor: '))
sleep(0.5)
while not d == 5:
    print('Você deseja:')
    print('[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n''[ 4 ] Novos números\n[ 5 ] Sair do programa')
    d = int(input('====> '))
    print(15 * '-=-')
    if d == 1:
        print('A soma de {} com {} é {:.2f}'.format(v1, v2, v1 + v2))
    elif d == 2:
        print('A multiplicação de {} com {} é {:.2f}'.format(v1, v2, v1 * v2))
    elif d == 3:
        if v1 > v2:
            print('O maior valor é {}'.format(v1))
        else:
            print('O menor valor é {}'.format(v2))
    elif d == 4:
        v1 = float(input('Insira o 1º valor: '))
        v2 = float(input('Insira o 2º valor: '))
    elif d == 5:
        print('            Encerrando o programa            ')
    else:
        print(' * Opção inválida * ')
        print('  Tente novamente!  ')
    print(15 * '-=-')
    sleep(0.5)
# correto
