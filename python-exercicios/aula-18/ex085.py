valores = [[], []]
# inserção dos valores
for c in range(0 , 7):
    num = int(input(f'Insira o {c + 1}º valor: '))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
# ordenação das listas dos pares e impares
valores[0].sort()
valores[1].sort()
# print dos valores
print('-=-' * 20)
print(f'Os valores pares inseridos são: {valores[0]}')
print(f'Os valores ímpares inseridos são: {valores[1]}')
# correto
