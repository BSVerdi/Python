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
