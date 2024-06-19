from time import sleep
from datetime import date
print(15 * '-=-')
print('Analisador de maioridade')
print(15 * '-=-')
h = date.today().year
N = 0
n = 0
for c in range(1, 8):
    print('Insira o ano de nascimento da {}ª pessoa'.format(c))
    a = int(input('===> '))
    if h - a > 21:
        N += 1
    else:
        n += 1
print(10 * '-=-')
print('     Analisando os dados.')
print(10 * '-=-')
sleep(0.5)
print('''Há {} pessoas maiores de idade.
Há {} pessoas menores de idade.'''
      .format(N, n))
print(10 * '-=-')
# correto
