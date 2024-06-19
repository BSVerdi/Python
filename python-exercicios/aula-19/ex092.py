from datetime import date
dados = dict()
# coleção de dados
dados['Nome'] = str(input('Nome: ')).strip()
dados['Idade'] = date.today().year - int(input('Ano de nascimento: '))
dados['CTPS'] = int(input('Carteira de trabalho (0 se não possuir): '))
if not dados['CTPS'] == 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$ '))
    dados['Aposentadoria'] = dados['Idade'] - (date.today().year - dados['Contratação']) + 35
# print dos dados
print('-=-' * 20)
for k, v in dados.items():
    print(f'{k}: {v}')
print('-=-' * 20)
# correto
