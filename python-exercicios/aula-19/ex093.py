dados = dict()
gols = list()
# coleção dos dados
print('-=-' * 20)
dados['nome'] = str(input('Nome: ')).strip()
partidas = int(input(f'Quantas partidas {dados['nome']} jogou?: '))
for c in range(partidas):
    gols.append(int(input(f'Quantos gols na partida {c + 1}?: ')))
    dados['gols'] = gols[:]
    if c == 0:
        dados['total'] = gols[c]
    else:
        dados['total'] += gols[c]
# print dos dados
print('-=-' * 20)
print(dados)
print('-=-' * 20)
for k, v in dados.items():
    print(f'{k}: {v}')
print('-=-' * 20, f'\nO jogador {dados['nome']} jogou {partidas} partidas.')
for c in range(partidas):
    print(f'=> Na partida {c + 1}, fez {dados['gols'][c]} gols.')
print(f'Foi um total de {dados['total']} gols\n','-=-' * 20)
# correto
