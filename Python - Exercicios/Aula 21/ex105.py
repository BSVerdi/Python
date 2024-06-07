def notas(*num, sit=False):
    '''
    -> Função para analisar o desempenho de algum aluno
    :param num: uma ou mais notas do aluno (aceita varias)
    :param sit: (opcional) indica se deve mostrar ou não a situação do aluno
    :return: dicionario com os resultados
    '''
    aluno = dict()
    media = 0
    for c in range(len(num)):
        media += num[c]
        if c == 0:
            aluno['maior'] = aluno['menor'] = num[c]
        else:
            if num[c] > aluno['maior']:
                aluno['maior'] = num[c]
            elif num[c] < aluno['menor']:
                aluno['menor'] = num[c]
    aluno['media'] = media / len(num)
    if sit == True:
        if 0 <= aluno['media'] < 3:
            aluno['situação'] = 'Péssima'
        elif 3 <= aluno['media'] < 6:
            aluno['situação'] = 'Ruim'
        elif 6 <= aluno['media'] < 8:
            aluno['situação'] = 'Boa'
        elif 8 <= aluno['media'] <= 10:
            aluno['situação'] = 'Ótima'
    return aluno


# Main
dados = notas(10, 10, 10)
print(dados)
# correto
