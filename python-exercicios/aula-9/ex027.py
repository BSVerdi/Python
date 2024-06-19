n = str(input('Insira o nome de uma pessoa: ')).strip().title()
P = n.find(' ')
U = n.rfind(' ')
print('O primeiro nome é: {}\n'
      'O ultimo nome é: {}'
      .format(n[:P], n[U:])
      )
# correto
