import moeda

v = float(input('Insira um valor (R$): '))
print(f'A metade de {moeda.real(v)} é {moeda.metade(v, True)}')
print(f'O dobro de {moeda.real(v)} é {moeda.dobrar(v, True)}')
print(f'Aumentando {moeda.real(v)} em 15%, temos {moeda.aumentar(v, 15, True)}')
print(f'reduzindo {moeda.real(v)} em 7%, temos {moeda.aumentar(v, 7, True)}')
# correto
