lista = []
#inserção dos valores na lista
while True:
    lista.append(int(input('Insira um valor: ')))
    r = str(input('Deseja continuar? [S | N]: ')).strip().upper()
    while not r in 'SN':
        print('Opção invalida!\nTente novamente!')
        r = str(input('Deseja continuar? [S | N]: ')).strip().upper()
    if r == 'N':
        break
lista.sort(reverse = True)
#print dos resultados
print(f'Voce inseriu {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
# correto
