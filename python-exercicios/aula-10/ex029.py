v = float(input('Insira a velocidade do carro em km/h: '))
if v > 80:
    print('Você foi multado!\n'
          'A multa custará R${:.2f}'
          .format((v-80)*7)
          )
else:
    print('Parabéns! Você estava dentro do limite da pista!')
# correto
