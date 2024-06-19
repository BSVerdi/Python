alunos = list()
nomes = list()
notas = list()
media = 0
# inserção dos dados dos alunos
while True:
    nomes.append(str(input('Nome: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    nomes.append(notas[:])
    alunos.append(nomes[:])
    nomes.clear()
    notas.clear()
    r = str(input('Deseja Continuar? [S|N]: ')).strip()
    while not r in 'SsNn':
        print('Opção Inválida!\nTente Novamente!')
        r = str(input('Deseja Continuar? [S|N]: ')).strip()
    if r in 'Nn':
        break
# print do boletim
print('-=-' * 20,f'\n| Nº |{'Nome':^10}|{'Média':^8}|')
for c in range(len(alunos)):
    media = (alunos[c][1][0] + alunos[c][1][1]) / 2
    print(f'| {c + 1:02d} |{alunos[c][0]:^10}|{media:^8.2f}|')
# Print das notas separadas
while True:
    print(f'{'(-1 para interromper)':-^60}')
    r = int(input('Deseja ver as notas de qual aluno?: '))
    if r == -1:
        break
    while not r in range(len(alunos) + 1):
        print('Opção Inválida!\nTente Novamente!')
        print(f'{'(-1 para interromper)':-^60}')
        r = int(input('Deseja ver as notas de qual aluno?: '))
    print(f'As notas de {alunos[r - 1][0]} são {alunos[r - 1][1]}')
print('-=-' * 20,f'{'Finalizando...':^60}\n{' <<Volte Sempre!>> ':-^60}', '-=-' * 20)
# correto
