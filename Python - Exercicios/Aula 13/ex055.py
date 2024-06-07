n = ['', '', '', '', '']
for c in range(0, 5):
    print('Insira o {}º peso: '.format(c + 1), end='')
    n[c] = float(input(''))
p = sorted(n)
print(8 * '-=-')
print('O maior peso é de {}Kg'.format(p[4]))
print('O menor peso é de {}Kg'.format(p[0]))
print(8 * '-=-')
# correto
