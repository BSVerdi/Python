n = str(input('Isira um número de 0 a 9999: '))
N = n.zfill(4)
print('Unidade: {}\n'
      'Dezena : {}\n'
      'Centena: {}\n'
      'milhar : {}'
      .format((N[3]), (N[2]), (N[1]), (N[0]))
      )
# correto
