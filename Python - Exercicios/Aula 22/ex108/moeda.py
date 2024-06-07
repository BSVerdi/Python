def aumentar(v, p):
    return v + v * p / 100


def diminuir(v, p):
    return v - v* p / 100


def dobrar(v):
    return v * 2


def metade(v):
    return v / 2


def real(v):
    return f'R${v:.2f}'.replace('.', ',')