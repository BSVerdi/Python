c = str(input('Insira o comprimento de três segmentos de retas: ')).split()
c1 = float(c[0])
c2 = float(c[1])
c3 = float(c[2])
if (c1 + c2) > c3 and (c1 + c3) > c2 and (c2 + c3) > c1:
    print('É possível formar um triângulo com esses segmentos.')
else:
    print('Não é possível formar um triângulo com esses segmentos.')
# correto
