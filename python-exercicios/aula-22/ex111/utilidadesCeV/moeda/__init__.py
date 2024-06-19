def aumentar(v, p, real=False):
    v = v + v * p / 100
    if real == True:
        v = f'R${v:.2f}'.replace('.', ',')
    return v


def diminuir(v, p, real=False):
    v = v - v * p / 100
    if real == True:
        v = f'R${v:.2f}'.replace('.', ',')
    return v


def dobrar(v, real=False):
    v *= 2
    if real == True:
        v = f'R${v:.2f}'.replace('.', ',')
    return v


def metade(v, real=False):
    v /= 2
    if real == True:
        v = f'R${v:.2f}'.replace('.', ',')
    return v


def real(v):
    return f'R${v:.2f}'.replace('.', ',')


def resumo(v, pa, pr):
    print('---' * 20)
    print(f'{'RESUMO DO VALOR':^60}')
    print('---' * 20)
    print(f'{'Preço analisado:':<25}{real(v):>5}')
    print(f'{'Dobro do preço:':<25}{dobrar(v, True):>5}')
    print(f'{'Metade do preço:':<25}{metade(v, True):>5}')
    print(f'{pa}{'% de aumento:':<23}{aumentar(v, pa, True):>5}')
    print(f'{pr}{'% de redução:':<23}{aumentar(v, pr, True):>5}')
    print('---' * 20)
