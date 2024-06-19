lista = ('lápis' , 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.90, 'Mochila', 120.70, 'Canetas', 22.70, 'Livro', 34.90)
print('--' * 30)
print(f'{'Listagem de Preços':^60}')
print('--' * 30)
for c in lista:
    if type(c) == str:
        print(f'{c:.<50}', end='')
    else:
        print(f'{'R$'} {c:>6.2f}')
print('--' * 30)
#Correto
