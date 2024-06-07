lista = []
par = []
impar = []
# inserção dos valores e divisão em pares e impares
while True:
    num = int(input('Insira um valor: '))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)    
    r = str(input('Deseja continuar? [S | N]: ')).strip().upper()
    while not r in 'SN':
        print('Opção invalida!\nTente novamente!')
        r = str(input('Deseja continuar? [S | N]: ')).strip().upper()
    if r == 'N':
        break
# print dos resultados
print('-=-' * 20)
print(f'Lista completa: {lista}')
print(f'Lista dos pares: {par}')
print(f'Lista dos impares: {impar}')
print('-=-' * 20)
# correto
