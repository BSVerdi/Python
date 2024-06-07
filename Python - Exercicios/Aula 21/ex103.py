def ficha(nome, gols):
    dados = dict()
    if nome == '':
        dados['nome'] = "<Desconhecido>"
    else:
        dados['nome'] = nome
    if gols.isnumeric():
        dados['gols'] = gols
    else:
        dados['gols'] = 0
    return dados


# Main
nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
dados = ficha(nome, gols)
print(f'O jogador {dados['nome']} fez {dados['gols']} gol(s) no campeonato.')
# correto
