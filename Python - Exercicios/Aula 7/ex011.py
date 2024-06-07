h = float(input('Insira a altura em metros da parede: '))
l = float(input('Insira a largura em metros da parede: '))
print('A area dessa parede é: {:.2f}m2 \n'
      'Já a  quantidade de tinta nescessária para pintar essa parede é: {:.2f}L'
      .format(h*l, (h*l)/2))
# correto
