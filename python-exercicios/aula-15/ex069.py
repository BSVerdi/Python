mi = 0
h = 0
m = 0
while True:
    print('-' * 30)
    print('     CADASTRE UMA PESSOA')
    print('-' * 30)
    i = int(input('Idade: '))
    if i > 18:
        mi += 1
    while True:
        s = str(input('Sexo: [M/F] ')).lower()
        if s == 'm' or s == 'f':
            break
    if s == 'm':
        h += 1
    elif s =='f' and i < 20:
        m += 1 
    print('-' * 20)
    while True:
        d = str(input('Quer continuar? [S/N] ')).lower()
        if d == 's' or d =='n':
            break
    if d == 'n':
        break
print('====== Fim do Programa ======')
print(f'Total de pessoas com mais de 18 anos: {mi}')
print(f'Ao todo temos {h} homens cadastrados.')
print(f'E temos {m} mulheres com menos de 20 anos.')
#Correto
