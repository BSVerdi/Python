import moeda

v = float(input('Insira um valor (R$): '))
print(f'A metade de {moeda.real(v)} é {moeda.real(moeda.metade(v))}')
print(f'O dobro de {moeda.real(v)} é {moeda.real(moeda.dobrar(v))}')
print(f'Aumentando {moeda.real(v)} em 15%, temos {moeda.real(moeda.aumentar(v, 15))}')
print(f'Reduzindo {moeda.real(v)} em 5%, temos {moeda.real(moeda.diminuir(v, 5))}')
# correto
