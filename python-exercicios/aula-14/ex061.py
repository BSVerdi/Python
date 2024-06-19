a1 = float(input('Insira o primeiro termo da PA: '))
r = float(input('Insira a razão da PA: '))
a = 0
while a != 10:
    t = a1 + r * a
    a += 1
    print(t, end=' => ')
print('Fim')
# correto
