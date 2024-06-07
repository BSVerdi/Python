from time import sleep
print(15 * '-=-')
print('{} Tabuada {}'.format(18 * '=', 18 * '='))
print(15 * '-=-')
n = int(input('insira um número inteiro: '))
print(15 * '-=-')
print('Fazendo a tabuada do {}'.format(n))
print(15 * '-=-')
sleep(0.5)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n * c))
    sleep(0.5)
# correto
