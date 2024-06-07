from time import sleep
from datetime import date
a = int(str(date.today())[:str(date.today()).find('-')])
print('-=-' * 15)
print('Categorização de atletas')
print('-=-' * 15)
sleep(0.5)
n = str(input('Insira o ano de nascimento do atleta: ')).split()
an = int(n[2])
if (a - an) <= 9:
    r = 'mirim'
elif (a - an) <= 14:
    r = 'infatil'
elif (a - an) <= 19:
    r = 'júnior'
elif (a - an) <= 25:
    r = 'sênior'
else:
    r = 'master'
sleep(0.5)
print('-=-' * 20)
print('O atleta possui {} anos, logo é um atleta {}'.format((a - an), r))
print('-=-' * 20)
# correto
