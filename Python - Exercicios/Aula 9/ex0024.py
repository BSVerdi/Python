n = str(input('Insira o nome de uma cidade: ')).strip().title()
d = n.split()
print('O nome começa com "Santo": {}'.format('Santo' in d[0]))
# correto
