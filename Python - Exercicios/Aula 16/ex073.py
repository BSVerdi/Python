c = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Athletico-PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco da Gama', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG')
print('=-' * 40)
print(f'Os 5 primeiros são {c[0:5]}')
print('=-' * 40)
print(f'Os 4 últimos são {c[16:20]}')
print('=-' * 40)
print(f'Os times em ordem alfabética: {sorted(c)}')
print('=-' * 40)
print(f'O Cuiabá está na {c.index('Cuiabá') + 1}ª posição')
print('=-' * 40)
#Correto