ln = ()
for c in range(0 , 4):
    ln += (int(input('Digite um número: ')),)
print(f'O valor 9 apareceu {ln.count(9)} vezes.')
if 3 in ln:
    print(f'O valor 3 apareceu na {ln.index(3)}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram ', end='')
for n in ln:
    if n % 2 == 0:
        print(n, end=' ')
#Correto
