s = float(input('Insira o salário do funcionário: '))
if s > 1250.00:
    print('Analisando esse salário. Ele terá um aumento de 10%\n'
          'Após o aumento, o salário será R${:.2f}'.format(s*1.10)
          )
else:
    print('Analisando esse salário. Ele terá um aumento de 15%\n'
          'Após o aumento, o salário será R${:.2f}'.format(s*1.15)
          )
# correto
