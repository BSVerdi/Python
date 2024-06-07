d = 0
n = 0
s = 0
while not n == 999:
    n = int(input('Insira um valor inteiro: '))
    if n != 999:
        d += 1
        s += n
print('Foram inseridos {} valores e a soma total equivale a {}'.format(d, s))
# correto
