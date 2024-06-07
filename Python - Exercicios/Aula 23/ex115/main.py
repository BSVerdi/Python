import funcoes

pessoas = funcoes.ler()[:]
dados = dict()
while True:
    funcoes.titulo('MENU PRINCIPAL')
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair do Sistema')
    print('---' * 20)
    while True:
        opc = funcoes.leiaint('Sua opção: ')
        if opc in range(1, 4):
            break
        else:
            funcoes.erro('Insira uma opção válida.')
    if opc == 1:
        funcoes.tabela_nomes('PESSSOAS CADASTRADAS', funcoes.ler())
    elif opc == 2:
        funcoes.titulo('NOVO CADASTRO')
        dados['nome'] = funcoes.leianome('Nome: ')
        dados['idade'] = funcoes.leiaint('Idade: ')
        print(f'Novo registro de {dados['nome']} adicionado')
        pessoas.append(dados.copy())
        dados.clear()
        funcoes.salvar(pessoas)
    elif opc == 3:
        funcoes.titulo('< Finalizando >')
        break
# correto
