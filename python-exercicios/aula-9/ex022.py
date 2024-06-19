n = str(input('Insira seu nome completo: '))
d = n.split()
print('Seu nome em maiúsculas é: {}'.format(n.upper()))
print('Seu nome em minúsculas é: {}'.format(n.lower()))
print('Ao todo seu nome possui {} letras.'.format(len(''.join(d))))
print('Seu primeiro nome possui {} letras.'.format(len(d[0])))
# correto
