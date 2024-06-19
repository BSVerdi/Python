from time import sleep


def titulo(txt):
    print()
    print('---' * 20)
    print(f'{txt:^60}')
    print('---' * 20)
    print()


# Main
while True:
    titulo('Sistema de Ajuda PyHELP')
    funçao_blibioteca = input('Função ou Blibioteca => ')
    if funçao_blibioteca == 'fim':
        titulo('Até Logo!')
        break
    sleep(0.5)
    titulo(f'Acessando o manual do comando {funçao_blibioteca}')
    sleep(0.5)
    help(funçao_blibioteca)
# correto
