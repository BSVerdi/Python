f = ''.join(str(input('Insira sua frase aqui: ')).strip().lower().split())
t = int(len(''.join(f)))
for c in range(0, t):
    if (f[c]) == (f[(t - 1) - c]):
        r = 'é um palindromo'
    else:
        r = 'não é um palindromo'
print('Analisando a frase, {}'.format(r))
# correto
