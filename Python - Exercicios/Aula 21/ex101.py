def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if 65 > idade >= 18:
        return f'com {idade} anos: VOTO OBRIGATÓRIO.'
    elif 18 > idade >= 16 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    elif idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
        

# Main
print('-=-' * 20)
resp = voto(int(input('Em que ano você nasceu?: ')))
print(resp)
# correto
