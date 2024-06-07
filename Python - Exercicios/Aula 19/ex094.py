dados = dict()
pessoas = list()
media = 0
# coleção de dados
while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo [M | F]: ')).strip()
    while not dados['sexo'] in 'MmFf':
        print('Opção Inválida\nTente Novamente!')
        dados['sexo'] = str(input('Sexo [M | F]: ')).strip()
    dados['idade'] = int(input('Idade: '))
    media += dados['idade']
    opc = str(input('Deseja Continuar [S | N]: ')).strip()
    pessoas.append(dados.copy())
    dados.clear()
    while not opc in 'SsNn':
        print('Opção Inválida\nTente Novamente!')
        opc = int(input('Deseja Continuar [S | N]: ')).strip()
    if opc in 'Nn':
        break
media /= len(pessoas)
# print dos resultados
print('-=-' * 20, f'=> O grupo tem {len(pessoas)} pessoas.')
print(f'=> A média de idade é de {media:.2f} anos.')
print(f'=> As mulheres cadastradas foram: ',end='')
# mulheres cadastradas
for d in pessoas:
    if d['sexo'] in 'Ff':
        print(d['nome'],end=' ')
print('\n=> Lista das pessoas com idade acima da média:')
# pessoas com idade acima da media
for i in pessoas:
    if i['idade'] > media:
        print('=> ',end='')
        for k, v in i.items():
            print(f'{k} = {v}; ',end='')
        print()
print(f'{'< Encerrado >':-^60}')
# correto
