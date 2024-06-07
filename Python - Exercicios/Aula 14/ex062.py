a1 = float(input('Insira o primeiro termo da PA: '))
r = float(input('Insira a razão da PA: '))
a = 0
d = 10
while d != 0:
    for a in range(0, d):
        t = a1 + r * a
        print(t, end=' => ')
    print('Fim')
    print('Acima estão os {} primeiros termos dessa PA.'.format(d))
    D = int(input('Deseja ver mais quantos termos? '))
    if D != 0:
        d += D
    else:
        d = 0
# correto
