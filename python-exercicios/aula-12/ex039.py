from time import sleep
from datetime import date
a = str(date.today().year)
print('-=-' * 7)
print(' Alistamento militar ')
print('-=-' * 7)
sleep(0.5)
n = str(input('Insira sua data de nascimento: ')).split()
g = str(input('''insira seu genero
[ 1 ] - Masculino
[ 2 ] - Feminino
======> '''))
i = (int(a) - (int(n[2])))
if g == '1':
    if i == 18:
        print('já está na hora de você se alistar!')
    elif i < 18:
        f = 18 - i
        if f == 1:
            print('falta 1 ano para você se alistar!')
        else:
            print('falta {} anos para você se alistar'.format(f))
    else:
        p = i - 18
        if p == 1:
            print('já passou 1 ano do seu alistamento')
        else:
            print('ja passou {} anos do seu alistamento'.format(p))
else:
    print('Já que você é mulher, não precisa se alistar!')
# correto
