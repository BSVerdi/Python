n = str(input('Insira três numeros quaisquer: ')).split()
n1 = float(n[0])
n2 = float(n[1])
n3 = float(n[2])
print('Analisando esse números')
if n1 > n2 > n3:
    print('O maior deles é {}\n'
          'O menor deles é {}'
          .format(n1, n3)
          )
if n1 < n2 < n3:
    print('O maior deles é {}\n'
          'O menor deles é {}'
          .format(n3, n1)
          )
if n2 > n1 > n3:
    print('O maior deles é {}\n'
          'O menor deles é {}'
          .format(n2, n3)
          )
if n2 < n1 < n3:
    print('O maior deles é {}\n'
          'O menor deles é {}'
          .format(n3, n2)
          )
if n2 > n3 > n1:
    print('O maior deles é: {}\n'
          'O menor deles é {}'
          .format(n2, n1)
          )
if n2 < n3 < n1:
    print('O maior deles é {}\n'
          'O menor deles é {}'
          .format(n1, n2)
          )
# correto
