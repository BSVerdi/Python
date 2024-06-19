from time import sleep
print(6 * '-=-')
print('Calculadora de IMC')
print(6 * '-=-')
sleep(0.5)
m = str(input('Insira seu peso em Kg e sua altura em m: ')).split()
imc = float(m[0]) / (float(m[1])**2)
if imc < 18.5:
    r = 'abaixo do peso.'
elif 18.5 <= imc < 25:
    r = 'no peso ideal'
elif 25 <= imc < 30:
    r = 'em sobrepeso'
elif 30 <= imc < 40:
    r = 'em estado de obesidade'
else:
    r = 'em estado de obesidade mórbida'
sleep(0.5)
print(32 * '-=-')
print(
    'Analisando os dados, o indivíduo possui um IMC de {:.1f}, estando {}!'
    .format(imc, r)
)
print(32 * '-=-')
# correto
