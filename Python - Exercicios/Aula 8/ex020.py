from random import sample
n = (input('Insira o primeiro nome: '),
     input('Insira o segundo nome: '),
     input('Insira o terceiro nome: '),
     input('Insira o quarto nome: ')
     )
print('A ordem de apresentação será: {}'.format(sample(n, k=len(n))))
# correto
