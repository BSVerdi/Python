import pygame
from random import choice
from time import sleep
pygame.init()
a = ('ex021.mp3')
b = ('ex021b.mp3')
e = str(choice([a, b]))
pygame.mixer.music.load(e)
print('Uma música aleatória será escolhida.')
sleep(1)
if e == a:
    print('A musica escolhida foi Ritmo de treino!'),
    pygame.mixer.music.play(),
    sleep(127),
    print('Gostou do resultado? Caso tenha gostado tente novamente!')
else:
    print('A música escolhida foi Whonder where you are!'),
    pygame.mixer.music.play(),
    sleep(396),
print('Gostou do resultado? Caso tenha gostado tente novamente!')
