from time import sleep

r = ''
while r != 'M' and r !='F':
    r = str(input('Insira seu gênero [ M ] | [ F ]: ')).upper().strip()[0]
    if r != 'M' and r != 'F':
        print(' * Opção Inválida * ')
        sleep(0.5)
        print('  Tente Novamente!')
        sleep(0.5)
print('Obrigado pela resposta!')
# Correto
