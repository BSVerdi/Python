# codigo errado
'''from math import sin, cos, tan
a = (float(input('Insira o valor de um ângulo: ')))
print('Sobre esse ângulo:\n'
      'Seu seno vale: {:.2f}\n'
      'Seu cosseno vale: {:.2f}\n'
      'Sua tangente vale: {:.2f}'
      .format(sin(a), cos(a), tan(a))
      )'''

# correção
from math import sin, cos, tan, radians
a = (float(input('insira o valor de um ângulo: ')))
print('Sobre esse ângulo:\n'
      'Seu seno vale: {:.2f}\n'
      'Seu cosseno vale: {:.2f}\n'
      'Sua Tangente vale: {:.2f}\n'
      .format(sin(radians(a)), cos(radians(a)), tan(radians(a))))
