matriz = [[], [], []]
# inserção dos valores da matiz
for c in range(0, 9):
    matriz[int(c / 3)].append(int(input(f'Insira um valor para [{int(c / 3)}, {c % 3}]: ')))
print('-=-' * 20)
# print da matriz
for i in range(0 , 3):
    for j in range(0 , 3):
        print(f'[ {matriz[i][j]:03d} ]', end='')
    print(end='\n')
# correto
