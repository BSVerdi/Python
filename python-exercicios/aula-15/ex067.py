while True:
    t = int(input('Quer ver a tabuada de qual valor? '))
    if t < 0:
        break
    print('-' * 20)
    for c in range(1 , 11):
        print(f'{t} X {c} = {t * c}')
    print('-' * 20)
print('Programa tabuada encerrado!! Volte sempre.')
#Correto
