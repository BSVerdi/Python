import moeda

v = float(input('Insira um valor (R$): '))
print(f'A metade do preço R${v:.2f} é R${moeda.metade(v):.2f}')
print(f'O dobro do preço R${v:.2f}  é R${moeda.dobro(v):.2f}')
print(f'Aumentando 10%, temos R${moeda.aumentar(v, 10):.2f}')
print(f'Reduzindo 13%, temos R${moeda.diminuir(v, 13):.2f}')
# correto
