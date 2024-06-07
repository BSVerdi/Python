from time import sleep
s = 0
for c in range(0, 6):
    n = int(input('Insira um número inteiro: '))
    if n % 2 == 0:
        s += n
print(18 * '-=-')
print('A soma dos números pares inseridos equivale a {}'.format(s))
print(18 * '-=-')
# correto
