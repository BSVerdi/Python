print('-=-' * 8)
print('Validação de empréstimos')
print('-=-' * 8)
V = float(input('Insira o valor da casa: R$'))
S = float(input('Insira seu salário: R$'))
T = float(input('Insira em quantos anos deseja pagar: '))
P = V / (T * 12)
if P > (S * 0.3):
    r = 'não é possível realizar o empréstimo'
else:
    r = 'é possível realizar o empréstimo'
print('-=-' * 20)
print('Após analisar a situação, {}'.format(r))
print('-=-' * 20)
# correto
