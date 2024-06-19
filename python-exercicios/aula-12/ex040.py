from time import sleep
print('-=-' * 8)
print('Analisador de notas')
print('-=-' * 8)
sleep(0.5)
n = str(input('Insira as duas notas do aluno: ')).split()
m = (float(n[0]) + float(n[1]))/2
if m < 5:
    r = 'O aluno está reprovado!'
elif 5 <= m < 7:
    r = 'O aluno está em recuperação!'
else:
    r = 'O aluno está aprovado!'
sleep(0.5)
print('-=-' * 17)
print('''Analisando as notas, a média do aluno é {:.2f}.
{}'''.format(m, r))
print('-=-' * 17)
# correto
