from time import sleep
print('-=-' * 15)
print('Conversor de bases numéricas')
print('-=-' * 15)
n = int(input('Insira o número que deseja converter: '))
print('-=-' * 15)
sleep(0.5)
o = str(input('Insira 1 para binário\n'
              'Insira 2 para Octal \n'
              'Insira 3 para Hexadecimal\n'
              '==> '))
if o == '1':
    t = 'binário'
    r = bin(n)[2:]
elif o == '2':
    t = 'octal'
    r = oct(n)[2:]
else:
    t = 'hexadecimal'
    r = hex(n)[2:]
sleep(0.5)
print('-=-' * 15)
print('O valor {} convertido para {} é {}'.format(n, t, r))
print('-=-' * 15)
# correto
