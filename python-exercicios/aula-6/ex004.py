x = input('Digite algo: ')
print('Seu tipo primitivo é: {}'.format(type(x)))
print('Só tem espaços? {}'.format(x.isspace()))
print('É um númerico? {}'.format(x.isnumeric()))
print('É um alfabético? {}'.format(x.isalpha()))
print('É um alfanumérico? {}'.format(x.isalnum()))
print('Está em maiúsculas? {}'.format(x.isupper()))
print('Está em minúsculas? {}'.format(x.islower()))
print('Está capitalizada? {}'.format(x.istitle()))
# correto
