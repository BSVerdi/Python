print('-' * 30)
print('      Loja super Baratão')
print('-' * 30)
mp = t = s = c = 0
while True:
    np = str(input('Nome do Produto: '))
    p = float(input('Preço: R$'))
    c += 1 
    t += p
    if c == 1 or p < mp:
        mp = p
        pb = np
    if p > 1000:
        s += 1
    while True:
        d = str(input('Quer continuar? [S/N] ')).lower()
        if d == 's' or d =='n':
            break
    if d == 'n':
        break
print('{:-^40}'.format(' Fim do Programa '))
print(f'O total da compra foi R${t:.2f}')
print(f'Temos {s} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {pb} que custa R${mp:.2f}')
#Correto
