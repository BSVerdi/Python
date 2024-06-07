from time import sleep
def contador(a, b, c):
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if c == 0:
        c = 1
    if a > b:
        b -= 1
        if c > 0:
            c *= -1
    elif a < b:
        b += 1
    for c in range(a, b, c):
        print(f'{c} ', end='')
        sleep(0.3)
    print('Fim!')


print('-=-' * 20)
contador(1, 10, 1)
print('-=-' * 20)
contador(10, 0, 2)
print('-=-' * 20)
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
# correto
