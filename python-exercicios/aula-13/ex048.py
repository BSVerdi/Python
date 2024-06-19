s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
print(24 * '-=-')
print('A soma dos números impares multiplos de 3 entre 1 e 500 é igual a {}'
      .format(s))
print(24 * '-=-')
# correto
    