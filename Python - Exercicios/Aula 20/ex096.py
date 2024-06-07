def area(a, b):
    print(f'A área do terreno de {a}mx{b}m é de {a * b}m².')


print('=-=' * 20)
print(f'{'Controle de Terrenos'}')
print('=-=' * 20)
area(float(input('Largura(m): ')), float(input('Comprimento(m): ')))
# correto
