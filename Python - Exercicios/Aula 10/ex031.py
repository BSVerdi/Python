print('---|Calculadora de preço para viajens|---')
d = float(input('Insira a distância da viajem em Km: '))
if d <= 200:
    print('O preço da viajem será de R${:.2f}'.format(d*0.5))
else:
    print('O preço da viajem será de R${:.2f}'.format(d*0.45))
# correto
