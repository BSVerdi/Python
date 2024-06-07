p = []
# inserção da expressão
conta = str(input('Insira a expressão: '))
# separação dos parenteses em uma lista
for c in range(len(conta)):
    if conta[c] in '()':
        p.append(conta[c])
if not p.count('(') == p.count(')'):
    print('A expressão não é valida!')
else:
    print('A expressão é valida!')
# correto
