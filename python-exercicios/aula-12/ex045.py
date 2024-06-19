from random import choice
from time import sleep
print(20 * '-=-')
print('Tente me vencer no pedra, papel e tesoura!')
print(20 * '-=-')
c = choice(['Pedra', 'Papel', 'Tesoura'])
sleep(0.5)
j = str(input('faça sua escolha: ')).title().strip()
if c == 'Pedra' and j == 'Pedra' or c == 'Papel' and j == 'Papel' or c == 'Tesoura' and j == 'Tesoura':
    r = ('\033[33m Empate!\033[m')
elif c == 'Papel' and j == 'Pedra' or c == 'Tesoura' and j == 'Papel' or c == 'Pedra' and j == 'Tesoura':
    r = ('\033[31mDerrota!\033[m')
else:
    r = ('\033[34mVitória!\033[m')
print(20 * '-=-')
sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!')
sleep(0.5)
print(7 * '-=-')
print('|  Computador | {}\n'
      '|  Jogador    | {}\n'
      '|  {}   |'.format(c, j, r))
print(7 * '-=-')
# correto
