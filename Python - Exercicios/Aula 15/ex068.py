from random import randint

print('=-=' * 10)
print('Vamos jogar par ou impar!!')
print('=-=' * 10)
v = 0
while True:
    n = int(input('Diga um valor: '))
    d = str(input('Par ou ímpar [P/I] ')).strip().lower()[0]
    if d == 'p':
        dc = 'i'
    else:
        dc = 'P'
    nc = randint(0, 10)
    s = n + nc
    if s % 2 == 0:
        r = 'PAR'
    else:
        r = 'IMPAR'
    print('-' * 20)
    print(f'Você jogou {n} e o computador {nc}. Total de {s} deu {r}')
    print('-' * 20)
    if s % 2 == 0 and d == 'p':
        print('Você VENCEU!')
        v += 1
    elif s % 2 == 0 and d =='i':
        print('Você PERDEU!')
        break
    print('Vamos jogar novamente...')
    print('=-=' * 10)
print(f'GAME OVER! Você venceu {v} vezes.')
#Correto
