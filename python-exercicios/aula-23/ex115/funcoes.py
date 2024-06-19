def titulo(txt):
    print('---' * 20)
    print(f'{txt:^60}')
    print('---' * 20)


def tabela_nomes(nome ,lst):
    titulo(nome)
    for c in lst:
        print(f'      {c['nome']:.<40}{c['idade']} anos')


def salvar(lst):
    import json
    
    json_str = json.dumps(lst, indent=4)
    with open('Python\Python - Exercicios\Aula 23\ex115\dados.json', 'w') as file:
        file.write(json_str)
    file.close()
    

def ler():
    import json

    dados = list()
    with open('Python\Python - Exercicios\Aula 23\ex115\dados.json', encoding='utf-8') as file:
        dados = json.load(file)
    return dados


def erro(txt):
    print(f'\033[0;31mERRO: {txt}\033[m')


def leiaint(txt):
    while True:
        try:
            num = int(input(f'{txt}'))
        except:
            erro('Insira um valor inteiro válido.')
        else:
            break
    return num


def leianome(txt):
    while True:
        nome = str(input(f'{txt}'))
        if nome.replace(' ', '').isalpha():
            break
        else:
            erro('Insira um nome válido.')
    return nome
