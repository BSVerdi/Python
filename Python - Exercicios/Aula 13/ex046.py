from time import sleep
from emoji import emojize
print(12 * '-=-')
print(' Contagem para os fogos de atifício ')
print(12 * '-=-')
sleep(0.5)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('{} Aproveite os fogos! {}'.format(emojize(':fireworks:'), emojize(':fireworks:')))
# correto
