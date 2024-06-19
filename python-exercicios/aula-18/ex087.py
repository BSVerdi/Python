matriz = [[], [], []]
spar = sc3 = num =  0
# Inserção dos valores da matriz
for c in range(0, 9):
    num = int(input(f'Insira um valor para [{int(c / 3)}, {c % 3}]: '))
    matriz[int(c / 3)].append(num)
    if num % 2 == 0:
        spar += num
    if c % 3 == 2:
        sc3 += num       
# print da matriz
print('-=-' * 20)
for i in range(len(matriz)):
    for j in range(len(matriz)):
        print(f'[ {matriz[i][j]:02d} ]',end='')
    print(end='\n')
print('-=-' * 20)
print(f'A soma dos valores pares é {spar}')
print(f'A soma dos valores da terceira coluna é {sc3}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
# correto
