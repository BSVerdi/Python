def leiaint(txt):
    while True:
        try:
            v = int(input(f'{txt}'))
        except (TypeError,  ValueError):
            print(f'\033[0;31mERRO: por favor, insira um valor inteiro válido.\033[m')
        except KeyboardInterrupt:
            print(f'\033[0;31mO usuário preferiu por não inserir o valor.\033[m')
            v = 0
        else: break
    return v 


def leiafloat(txt):
    while True:
        try:
            v = float(input(f'{txt}'))
        except (TypeError, ValueError):
            print(f'\033[0;31mERRO: por favor, insira um valor inteiro válido.\033[m')
        except KeyboardInterrupt:
            print(f'\033[0;31mO usuário preferiu por não inserir o valor.\033[m')
            v = 0
        else: break
    return v


# Main
vi = leiaint('Insira um valor inteiro: ')
vf = leiafloat('Insira um valor real: ')
print(f'O valor inteiro inserido foi {vi} e o real {vf}')
# correto
