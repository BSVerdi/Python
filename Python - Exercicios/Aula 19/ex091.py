from random import randint
from time import sleep

dados = list()
jogadores = dict()
aux = 0
print(f'{'< Valores Sorteados >':-^60}')
# Sorteamento de faces
for c in range(1 , 5):
    jogadores['num'] = c
    jogadores['face'] = randint(1, 6)
    print(f'O jogador {jogadores['num']} tirou {jogadores['face']}')
    sleep(0.5)
    dados.append(jogadores.copy())
# ordenação dos jogadores
for c in range(0 , 3):
    if dados[c]['face'] > dados[c + 1]['face']:
        aux = dados[c + 1]
        dados[c + 1] = dados[c]
        dados[c] = aux
print(f'{'< Ranking dos Jogadores >':-^60}')
for c in range(3, -1, -1):
    print(f'{4 - c}º lugar: Jogador {dados[c]['num']} com  {dados[c]['face']}')
    sleep(0.5)
print('---' * 20)
# correto
