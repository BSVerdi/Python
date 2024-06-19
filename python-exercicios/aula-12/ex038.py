print('-=-' * 15)
print('Comparador de números inteiros')
print('-=-' * 15)
n = str(input('Insira os dois números: ')).strip().split()
if (int(n[0])) > (int(n[1])):
    r = 'o primeiro é maior que o segundo.'
elif (int(n[0])) < (int(n[1])):
    r = 'o segundo número é maior que o primeiro'
else:
    r = 'os dois números são iguais.'
print('-=-' * 30)
print('Analisando os valores {} e {}, conclui-se que {}'.format(n[0], n[1], r))
print('-=-' * 30)
# correto
