from customtkinter import *

app = CTk()
app.title('Jogo da Velha')
app.geometry('420x550')
app.resizable(False, False)
set_appearance_mode('dark')

# frames
jogo = CTkFrame(master = app, height=400, width=400,corner_radius=5, fg_color='white')
jogo.pack(expand=True)

informações = CTkFrame(master = app, height=100, width=400,corner_radius=5, fg_color='white')
informações.pack(expand=True)

placar = CTkFrame(master = informações, height=90, width=270, border_width=2, border_color='black', fg_color='white')
placar.place(x=120, y=5)

jogador_X = CTkLabel(master = placar, text='X', text_color='#E01900', font=('Arial', 75), height=80, width=80)
jogador_X.place(x=20, y=5)
jogador_X_pontos = CTkLabel(master = placar, text='0', text_color='black', font=('Arial', 40), height=80, width=20)
jogador_X_pontos.place(x=100, y=5)
jogador_O = CTkLabel(master = placar, text='O', text_color='#1E2DB6', font=('Arial', 75), height=80, width=80)
jogador_O.place(x=170, y=5)
jogador_O_pontos = CTkLabel(master = placar, text='0', text_color='black', font=('Arial', 40), height=80, width=20)
jogador_O_pontos.place(x=150, y=5)
jogador_separador = CTkLabel(master = placar, text=':', text_color='black', font=('Arial', 35), height=80, width=8)
jogador_separador.place(x=131, y=5)

# tabuleiro

vertical = CTkLabel(master = jogo, text='', height=370, width=5, bg_color='black', anchor='center')
vertical.place(x=135, y=15)
vertical = CTkLabel(master = jogo, text='', height=370, width=5, bg_color='black', anchor='center')
vertical.place(x=260, y=15)
horizontal = CTkLabel(master = jogo, text='', width=370, height=1, bg_color='black', font=('Ivy', 5), anchor='center')
horizontal.place(x=15, y=135)
horizontal = CTkLabel(master = jogo, text='', width=370, height=1, bg_color='black', font=('Ivy', 5), anchor='center')
horizontal.place(x=15, y=260)


#---------------------------> Main <-----------------------------
tabuleiro = [['', '', ''], ['', '', ''], ['', '', '']]
jogadas = 0
jogador =''
pontos_x = 0
pontos_o = 0
partida = 0

def iniciar_jogo():
    def posicao(i, j, jogada):
        global jogadas
        global jogador
        global tabuleiro
        global partida
        
        if partida % 2 == 0:
            if jogadas % 2 == 0:
                jogador = 'X'
            else:
                jogador = 'O'
        else:
            if jogadas % 2 == 0:
                jogador = 'O'
            else:
                jogador = 'X'

        # jogada
        if jogada.cget('text') == '':
            tabuleiro[i][j] = jogador
            jogada.configure(text=jogador)
            if jogador == 'X':
                jogada.configure(text_color='#E01900')
            else:
                jogada.configure(text_color='#1E2DB6')
            jogadas += 1

        # inicio da checagem de vitoria
        if jogadas > 3:
            for c in range(0, 3):
                if tabuleiro[c][0] == tabuleiro[c][1] == tabuleiro[c][2] != '':
                    vitoria()
                elif tabuleiro[0][c] == tabuleiro[1][c] == tabuleiro[2][c] != '':
                    vitoria()
            if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != '':
                vitoria()
            elif tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != '':
                vitoria()
                
        # Possivel velha
        if jogadas == 9:
            limpar_tabuleiro()
            jogadas = 0
        

    def vitoria():
        global jogadas  
        global pontos_x
        global pontos_o
        global jogador

        if jogador == 'X':
            pontos_x += 1
            jogador_X_pontos.configure(text=str(pontos_x))
        elif jogador == 'O':
            pontos_o += 1
            jogador_O_pontos.configure(text=str(pontos_o))
        jogadas = 0

        limpar_tabuleiro()


    def limpar_tabuleiro():
        global tabuleiro
        global partida

        for i in range(0, 3):
            for j in range(0, 3):
                tabuleiro[i][j] = ''
        posicao_0.configure(text='')
        posicao_1.configure(text='')
        posicao_2.configure(text='')
        posicao_3.configure(text='')
        posicao_4.configure(text='')
        posicao_5.configure(text='')
        posicao_6.configure(text='')
        posicao_7.configure(text='')
        posicao_8.configure(text='')
        partida += 1
        
        
        
    #----> interface <----
    
    # linha 1
    posicao_0 = CTkButton(master = jogo, command=lambda:posicao(0, 0, posicao_0), text='', width=110, height=110, font=('Ivy', 90), fg_color='white', hover_color='gray')
    posicao_0.place(x=20, y=20)
    posicao_1 = CTkButton(master = jogo, command=lambda:posicao(0, 1, posicao_1), text='', width=110, height=110, font=('Ivy', 90), fg_color='white', hover_color='gray')
    posicao_1.place(x=145, y=20)
    posicao_2 = CTkButton(master = jogo, command=lambda:posicao(0, 2, posicao_2), text='', width=110, height=110, font=('Ivy', 90), fg_color='white', hover_color='gray')
    posicao_2.place(x=270, y=20)

    # linha 2
    posicao_3 = CTkButton(master = jogo, command=lambda:posicao(1, 0, posicao_3), text='', width=110, height=110, font=('Ivy', 90), fg_color='white', hover_color='gray')
    posicao_3.place(x=20, y=145)
    posicao_4 = CTkButton(master = jogo, command=lambda:posicao(1, 1, posicao_4), text='', width=110, height=110, font=('Ivy', 90), fg_color='white', hover_color='gray')
    posicao_4.place(x=145, y=145)
    posicao_5 = CTkButton(master = jogo, command=lambda:posicao(1, 2, posicao_5), text='', width=110, height=110, font=('Ivy', 90), fg_color='white', hover_color='gray')
    posicao_5.place(x=270, y=145)

    # linha 3
    posicao_6 = CTkButton(master = jogo, command=lambda:posicao(2, 0, posicao_6), text='', width=110, height=110, font=('Ivy', 90), fg_color='white', hover_color='gray')
    posicao_6.place(x=20, y=270)
    posicao_7 = CTkButton(master = jogo, command=lambda:posicao(2, 1, posicao_7), text='', width=110, height=110, font=('Ivy', 90), fg_color='white', hover_color='gray')
    posicao_7.place(x=145, y=270)
    posicao_8 = CTkButton(master = jogo, command=lambda:posicao(2, 2, posicao_8), text='', width=110, height=110, font=('Ivy', 90), fg_color='white', hover_color='gray')
    posicao_8.place(x=270, y=270)

# jogar
botão_jogar = CTkButton(master = informações, text='Jogar', text_color='black', font=('Arial', 20), width=100, height=30, corner_radius=5, anchor='center', fg_color='green', hover_color='darkgreen', command=iniciar_jogo)
botão_jogar.place(x=10, y=35)

app.mainloop()
