from time import sleep
def maior(* num):
    mn = 0
    print('Analisando os valores passados...')
    for c in num:
        print(f'{c} ', end='')
        sleep(0.3)
        if c > mn:
            mn = c
    print(f'Foram informandos {len(num)} valores ao todo.')   
    print(f'O maior valor informado foi {mn}.')


print('-=-' * 20)
maior(2, 9, 4, 5, 7, 1)
print('-=-' * 20)
maior(4, 7, 0)
print('-=-' * 20)
maior(1, 2)
print('-=-' * 20)
maior(6)
print('-=-' * 20)
maior(0)
print('-=-' * 20)
# correto
