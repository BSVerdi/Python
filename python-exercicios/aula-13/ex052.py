n = int(input('Insira um número inteiro: '))
s = 0
for c in range(1, n+1):
    if n % c == 0:
        s += c
if s == n + 1:
    r = 'ele é primo.'
else:
    r = 'ele não é primo.'
print('Analisando esse número, {}'.format(r))
# correto
