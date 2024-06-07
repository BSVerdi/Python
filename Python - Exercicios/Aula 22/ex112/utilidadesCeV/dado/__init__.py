def leiadinheiro(v):
    while True:
        valor = input(f'{v}').strip()
        if valor.replace(',', '').replace('.', '').isnumeric():
            break
        else: 
            print(f'\033[0;31mERRO: {valor} é um preço inválido.\033[m')
    return float(valor.replace(',', '.'))
