D = int(input('Por quantos dias o carro foi alugado? '))
d = float(input('Quantos quilometros foram percorridos durante esses dias? '))
print('O preço final a se pagar é de R${:.2f}'.format((60 * D) + (0.15 * d)))
# correto
