jogadores = list()
dados = dict()
gols = list()
# coleção de dados
print('-=-' * 20)
while True:
    dados['nome'] = str(input('Nome do Jogador: ')).strip()
    partidas = int(input(f'Quantas partidas {dados['nome']} jogou?: '))
    for c in range(partidas):
        gols.append(int(input(f'Quantos gols na partida {c + 1}?: ')))
        dados['gols'] = gols[:]
        if c == 0:
            dados['total'] = gols[c]
        else:
            dados['total'] += gols[c]
    dados['partidas'] = partidas
    jogadores.append(dados.copy())
    gols.clear()
    opc = str(input('Deseja Continuar [S | N]: ')).strip()
    while not opc in 'SsNn':
        print('Opção Inválida\nTente Novamente!')
        opc = str(input('Deseja Continuar [S | N]: ')).strip()
    if opc in 'Nn':
        break
# print dos dados dos jogadores
print(f'{'Cod':^5}{'Nome':^12}{'Gols':^12}{'Total':^5}')
print('---' * 20)
ctg = 1
for c in jogadores:
    print(f' {ctg:03d} {c['nome']:^12} {str(c['gols']):^12} {c['total']:^5}')
    ctg += 1
# print dos dados dos jogadores separados
while True:
    print(f'{'< (-1 para interromper >)':-^60}')    
    while True:
        cod = int(input('Deseja mostrar dados de qual jogador?: ')) - 1
        if cod in range(len(jogadores)) or cod == -2:
            break
        print('Opção Inválida\nTente Novamente!')
    if cod == -2:
        break
    print(f'Levantamento do jogador {jogadores[cod]['nome']:}:')
    for c in range(jogadores[cod]['partidas']):
        print(f'=> No jogo {c + 1} fez {jogadores[cod]['gols'][c]} gols.')
    print(f'Foi um total de {jogadores[cod]['total']} gols.')
print(f'{'< Encerrando >':-^60}')
# correto
