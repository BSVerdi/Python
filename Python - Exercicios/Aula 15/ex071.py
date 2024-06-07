print('=' * 30)
print('       Banco do Brenao')
print('=' * 30)
s = int(input('Que valor você quer sacar? R$'))
c = v = d = u = 0
while True:
    c = s // 50
    rc = s % 50
    if rc == 0:
        break
    v = rc // 20
    rv = rc % 20
    if rv == 0:
        break
    d = rv // 10
    rd = rv % 10
    if rd == 0:
        break
    u = rd // 1
    ru = rd % 1
    if ru == 0:
        break
print('=' * 30)
if c > 0:
    print(f'Total de {c} cédulas de R$50,00')
if v > 0:
    print(f'Total de {v} cédulas de R$20,00')
if d > 0:
    print(f'Total de {d} cédulas de R$10,00')
if u > 0:
    print(f'Total de {u} cédulas de R$1,00')
print('=' * 30)
print('Volte sempre ao Banco do Brenao! Tenha um bom dia!')
#Correto
