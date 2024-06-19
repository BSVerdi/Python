from time import sleep
from random import randint

qtd = 0
jogos = list()
total = list()
print('---' * 20)
print(f'{'JOGA NA MEGA SENA':^60}')
print('---' * 20)
# Inserção da quantidade de jogos e sorteamente dos numeros
qtd = int(input('Insira quantos jogos deseja realizar: '))
for c in range(0 ,qtd):
    for j in range(0, 6):
        jogos.append(randint(1, 61))
    total.append(jogos[:])
    jogos.clear()
# print dos jogos
print('-=-' * 7 ,f'Sorteando {qtd} Jogos', '-=-' * 7 )
for c in range(0, qtd):
    print(f'Jogo {c + 1}: {total[c]}')
    sleep(0.5)
print(f'{' <Boa Sorte> ':-^60}')
# correto
