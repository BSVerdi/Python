from random import choice
n = choice([0, 1, 2, 3, 4, 5])
t = int(input('Tente adivinhar o número entre 0 e 5 que eu estou pensando: '))
if t == n:
    print('Parabéns! O número escolhido foi {} e você o acertou!'.format(n))
else:
    print('Inacreditavel! O número escolhido foi {} e você chutou {}.'.format(n, t))
# correto
