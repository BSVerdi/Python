import urllib
import urllib.request

# fora de data
try:
    site = urllib.request.urlopen("https://www.pudim.com.br")
except urllib.error.URLError:
    print(f'\033[0;31mO site não está acessível no momento.\033[m')
else:
    print('O site está acessível')
