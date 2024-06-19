from time import sleep
print('Aqui estão todos os números pares de 1 a 50')
for c in range(2, 51, 2):
    print('{} '.format(c), end='')
    sleep(0.5)
print('Fim')
# correto
