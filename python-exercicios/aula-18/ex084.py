pessoas = list()
dados = list()
pesadas = list()
leves = list()
r = ''
media = 0
# coleção de dados
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    media += dados[1]
    pessoas.append(dados[:])
    dados.clear()
    r = str(input('Deseja continuar? [S|N]: ')).strip()
    while not r in 'SsNn':
        print('Opção Inválida!\nTente Novamente!')
        r = str(input('Deseja continuar? [S|N]: ')).strip()
    if r in 'Nn':
        break
media /= len(pessoas) # media dos pesos
print('-=-' * 20)
print(f'Ao todo, foram cadastradas {len(pessoas)} pessoas.')
# coleção e vereficação dos pesos de acordo com a media
for p in pessoas:
    if p[1] > media:
        pesadas.append(p[0])
    else:
        leves.append(p[0])
print(f'As com peso acima da média são {str(pesadas).strip('[]')}')
print(f'As com peso menor ou igual à média são {str(leves).strip('[]')}')
# correto
