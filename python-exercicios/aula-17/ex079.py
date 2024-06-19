lista = []
while True:
    # inserção dos valores
    num = int(input('Insira um Valor: '))
    if not num in lista:
        lista.append(num)
    else:
        print('Valor duplicado, não sera adicionado.')
    r = str(input('Deseja continuar? [S|N]: ')).upper().strip()
    # condição de parada
    while not r in 'SN':
        print('Opção invalida!\nTente novamente!')
        r = str(input('Deseja continuar? [S|N]: ')).upper().strip()
    if r == 'N':
        break
lista.sort() # ordenação da lista
print('-=-' * 20)
print(f'Você inseriu os valores {lista}') #print do resultado
# correto
