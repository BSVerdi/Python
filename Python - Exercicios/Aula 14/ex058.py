from random import randint
from time import sleep

c = randint(0, 10)
r = -1
t = 0
while r != c:
    print('Tente adivinhar um número inteiro entre 0 e 10 que eu estou pensando!')
    r = int(input('====> '))
    t += 1
    if r != c:
        print('    Errou!!!    ')
        sleep(0.5)
        print('Tente novamente!')
    sleep(0.5)
print('Eu pensei no número {} e você inseriu o número {}.'.format(c, r))
print('Você acertou o número que pensei em {} tentativas!'.format(t))
# correto
