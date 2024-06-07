from random import randint

ln = ()
for c in range(0, 5):
    ln += (randint(0 , 10),)
print(f'Os valores sorteados foram: {ln}')
print(f'O maior valor sorteado foi {sorted(ln)[-1]}')
print(f'O menor valor sorteado foi {sorted(ln)[0]}')
#Correto
