from time import sleep
print(13 * '-=-')
print('Validação de existência de um triângulo')
print(13 * '-=-')
sleep(0.5)
c = str(input('Insira os três comprimentos dos segmentos de reta: ')).split()
c1 = float(c[0])
c2 = float(c[1])
c3 = float(c[2])
if (c1 + c2) > c3 and (c1 + c3) > c2 and (c2 + c3) > c3:
    if c1 == c2 == c3:
        r = 'é possível formar um triângulo equilatero.'
    elif c1 == c2 != c3 or c2 == c3 != c1 or c3 == c1 != c2:
        r = 'é possível formar um triângulo isóceles.'
    else:
        r = 'é possível formar um triângulo escaleno.'
else:
    r = 'não é possível formar um triângulo.'
sleep(0.5)
print(23 * '-=-')
print('Analisando os segmentos, {}'.format(r))
print(23 * '-=-')
# correto
