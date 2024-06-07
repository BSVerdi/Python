lista = []
aux = 0
for c in range(0, 5):
    num = int(input('Insira um valor: '))
    if c == 0:
        lista.append(num)
        print('Valor adicionado à lista')
    else:
        for c in range(len(lista)):
            if not num > lista[c]:
                lista.insert(c, num)
                print(f'Valor adicionado à posição {c}')
                break
            elif c == len(lista) - 1:
                lista.append(num)
                print('Valor adicionado ao final da lista')
                break
print('-=-' * 20,f'\nOs valores inseridos em ordem são {lista}')
# correto
