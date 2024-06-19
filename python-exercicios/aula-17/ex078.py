lista = []
pmax = pmin = ''
# inserção dos valores
for c in range(0, 5):
    lista.append(int(input(f'Insira o {c + 1}º valor:')))
print('=-=' * 20)
# posição dos maiores e menores valores
for p, v in enumerate(lista):
    if v == max(lista):
        pmax += (f'{p}' + '... ')
    elif v == min(lista):
        pmin += (f'{p}' + '... ')
# print dos resultados
print(f'Voce digitou os valores {lista}')
print(f'O maior valor é {max(lista)} e esta nas posições {pmax}')
print(f'O menor valor é {min(lista)} e esta nas posições {pmin}')
# correto
