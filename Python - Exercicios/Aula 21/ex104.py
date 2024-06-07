def leiaint(txt):
    while True:
        end = False
        num = input(f'{txt}')
        for c in range(len(num)):
            if num[c] in '0123456789':
                end = True
        if end == True:
            break
        else:
            print('\033[0;31mERRO! Insira um valor inteiro válido.\033[m')        
    return num


# Main
n = leiaint('Insira um valor: ')
print(f'Voce inseriu o valor {n}')
# correto
