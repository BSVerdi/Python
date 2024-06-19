dados = dict()
dados['Nome'] = str(input('Nome: ')).strip()
dados['Média'] = float(input('Média: '))
if dados['Média'] >= 7:
    dados['Situação'] = 'Aprovado'
else:
    dados['Situação'] = 'Reprovado'
print('-=-' * 20)
for k, v in dados.items():
    print(f'{k}: {v}')
print('-=-' * 20)
# correto
