f = str(input('Insira uma frase aqui: ')).strip().upper()
print('A letra "A" aparece {} vezes.\n'
      'A primeira letra "A" aparece na posição {}\n'
      'A ultima letra "A" aparece na posição {}'
      .format(f.count('A' [0:]), (f.find('A') + 1), (f.rfind('A') + 1))
      )
# correto
