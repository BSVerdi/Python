from time import sleep
print(12 * '-=-')
print('          Valor a ser pago')
print(12 * '-=-')
p = float(input('Insira o valor do produto: R$'))
print(12 * '-=-')
m = int(input('insira o método de pagamento:\n'
              '(1) - À vista: 10% desconto\n'
              '(2) - À vista no cartão: 5% desconto\n'
              '(3) - Em até 2x no cartão sem juros\n'
              '(4) - 3x ou mais no cartão com 20% de juros\n'
              '====> ')
        )
if m == 1:
    r = 'à vista será R${:.2f}'.format(p * 0.90)
elif m == 2:
    r = 'à vista no cartão será R${:.2f}'.format(p * 0.95)
elif m == 3:
    r = 'em 2x de R${:.2f} no cartão será R${:.2f}'.format(p/2, p)
elif m == 4:
    j = 1.20 * p
    sleep(0.5)
    print(14 * '-=-')
    t = int(input('Insira em quantas parcelas deseja pagar:\n'
                  '(1) - 3 parcelas de R${:.2f}\n'
                  '(2) - 4 parcelas de R${:.2f}\n'
                  '(3) - 5 parcelas de R${:.2f}\n'
                  '(4) - 6 parcelas de R${:.2f}\n'
                  '(5) - 7 parcelas de R${:.2f}\n'
                  '(6) - 8 parcelas de R${:.2f}\n'
                  '===> '
                  .format(j / 3, j / 4, j / 5, j / 6, j / 7, j / 8)
                  )
            )
    if t == 1:
        r = 'em 3x de R${:.2f} no cartão será de R${:.2f}'.format(j / 3, j)
    elif t == 2:
        r = 'em 4x de R${:.2f} no cartão será de R${:.2f}'.format(j / 4, j)
    elif t == 3:
        r = 'em 5x de R${:.2f} no cartão será de R${:.2f}'.format(j / 5, j)
    elif t == 4:
        r = 'em 6x de R${:.2f} no cartão será de R${:.2f}'.format(j / 6, j)
    elif t == 5:
        r = 'em 7x de R${:.2f} no cartão será de R${:.2f}'.format(j / 7, j)
    elif t == 6:
        r = 'em 8x de R${:.2f} no cartão será de R${:.2f}'.format(j / 8, j)
    else:
        r = '* OPÇÃO INVALIDA *, tente novamente!'
else:
    r = '* OPÇÃO INVALIDA *, tente novamente!'
sleep(0.5)
print(25 * '-=-')
print('O valor final a ser pago {}'.format(r))
print(25 * '-=-')
# correto
