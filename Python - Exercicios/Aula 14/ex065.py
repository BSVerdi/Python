s = 0
q = 0
r = ''
while not r == 'n':
    n = int(input('Insira um valor inteiro: '))
    q += 1
    s += n
    if q == 1:
        M = n
        m = n
    if n > M:
        M = n
    elif n < m:
        m = n
    print('Deseja continuar? [ s | n ]')
    r = str(input('===>')).strip().lower()
print('A média dos valores inseridos é {}\n'
      'O maior valor é {}\n'
      'O menor valor é {}'
      .format(s/q, M, m)
      )
# correto
