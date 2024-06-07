n = int(input('Insira um valor inteiro: '))
t = a = 0
while t < n:
    t += 1
    if t == 1:
        a = 0
    elif t == 2:
        a = 1
    elif t == 3:
        a1 = 1
        a2 = 0
        a = a1 + a2
    else:
        a2 = a1
        a1 = a
        a = a1 + a2
    print(a, end=' => ')
print('Fim')
if t > 1:
    print('Acima estão os {} primeiros termos da sequência de Fibonacci.'.format(t))
elif t == 0:
    print('Acima está nenhum termo da sequência de Fibonacci.')
else:
    print('Acima está o primeiro termo da sequência de Fibonacci.')
# correto
