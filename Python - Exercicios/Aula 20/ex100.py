from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(5):
        lista.append(randint(0, 10))
        print(f'{lista[c]} ',end='')
        sleep(0.3)
    print('Pronto!')


def somapar(lista):
    soma = 0
    for p in lista:
        if p % 2 == 0:
            soma += p
    print(f'Somando os valores pares de {lista}, temos {soma}')


num = list()
sorteia(num)
somapar(num)
# correto
