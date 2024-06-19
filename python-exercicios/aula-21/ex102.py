def fatorial(fat=1, show=False):
    """
    -> Calcula o fatorial de um número
    :param fat: o numero a ser calculado
    :param show: (opcional) define se a conta sera ou nao mostrada
    :return: O valor do fatorial de um numero.
    """
    conta = ''
    num = fat
    for c in range(2 , fat):
        fat *= c
    if show == True:
        for c in range(num, 0, -1):
            if c > 1:
                conta += f'{c} X '
            else:
                conta += f'{c} = {fat}'
        fat = conta
    return fat


# Main
print('-=-' * 20)
print(fatorial(5, True))
print('-=-' * 20)
print(fatorial(8))
print('-=-' * 20)
print(help(fatorial))
# correto
