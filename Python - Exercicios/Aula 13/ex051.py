from time import sleep
a1 = float(input('Insira o primeiro termo de uma PA: '))
r = float(input('Insira a razão dessa PA: '))
sleep(0.5)
print('Os primeiros 10 termos dessa PA são:')
sleep(0.5)
for c in range(0, 10):
    print('{}'.format(a1 + r * c), end=' => ')
    sleep(0.5)
print('fim')
# correto
