from time import sleep
li = []
nh = []
mv = []
Si = 0
h = 0
m = 0
M = 0
r = ''
print(15 * '-=-')
print('             Analisador de grupo')
print(15 * '-=-')
for c in range(0, 4):
    print('  Insira  o nome, idade e sexo da {}ª pessoa'.format(c + 1))
    print(15 * '-=-')
    n = str(input('Nome: ')).strip().title()
    i = int(input('Idade: '))
    Si += i
    print('[ 1 ] - Masculino')
    print('[ 2 ] - Feminino')
    s = int(input('====> '))
    if s == 1:
        nh += [n]
        li += [i]
        h += 1
    elif s == 2:
        if i > 20:
            M += 1
        else:
            m += 1
    else:
        r = 'error'
        break
if r == 'error':
    print(' * Opção invalida * ')
    sleep(0.5)
    print('  Tente novamente!  ')
else:
    print(15 * '-=-')
    print('             Analisando o grupo!')
    print(15 * '-=-')
    # média das idades
    print('A média de idade do grupo é de {} anos.'.format(Si/4))
    # homem mais velho do grupo
    if h != 0:
        for c in range(0, h):
            x = int(li.count(max(li)))
            if max(li) == li[c] and x == 1:
                mv = ['{} é o homem mais velho do grupo.'.format(nh[c])]
            elif max(li) == li[c] and 1 < x < h:
                mv += [nh[c]]
            elif max(li) == li[c] and x == h:
                mv = ['Todos os homens do grupo possuem a mesma idade.']
    else:
        mv = ['Não há homens no grupo.']

    if len(mv) == 1:
        print('{}'.format(mv[0]))
    elif len(mv) == 2:
        print('{} e {} são os homens mais velhos do grupo.'
              .format(mv[0], mv[1]))
    else:
        print('{}, {} e {} são os homens mais velhos do grupo.'
              .format(mv[0], mv[1], mv[2]))
    # mulheres abaixo de 20 anos
    if m == 0 and M == 0:
        print('Não há mulheres no grupo.')
    elif m == 0 and M > 0:
        print('Todas as mulheres no grupo tem mais de 20 anos.')
    elif m > 0 and M == 0:
        print('Todas as mulheres do grupo tem menos de 20 anos.')
    else:
        if m == 1:
            print('1 mulher tem menos de 20 anos.')
        else:
            print('{} mulheres tem menos de 20 anos.'.format(m))
# correto
