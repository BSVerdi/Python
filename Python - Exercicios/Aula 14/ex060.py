n = N = int(input('Insira um valor: '))
f = 1
while n != 1:
    f *= n
    n -= 1
print('O fatorial de {} é {}'.format(N, f))
# correto
