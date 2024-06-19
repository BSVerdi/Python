from random import choice
a1 = input('Insira o nome do primeiro aluno(a): ')
a2 = input('Insira o nome do segundo aluno(a): ')
a3 = input('Insira o nome do terceiro aluno(a): ')
a4 = input('Insira o nome do quarto aluno(a): ')
print('O aluno(a) escolhido(a) foi {}!'.format(choice([a1, a2, a3, a4])))
# correto
