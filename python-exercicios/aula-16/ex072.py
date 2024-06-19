numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete, dezoito, dezenove, vinte')
while True:
    num = int(input('Digite um numreo entre 0 e 20: '))
    if num in range(0 , 21):
        break
    print('Tente novamente!')
print(f'Você digitou o número {numeros[num]}')
#Correto
