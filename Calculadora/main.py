import customtkinter as ctk

valor_1 = ''
valor_2 = ''
operacao = ''
entrada = True
resultado = 0

class Screen(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.conteudo = ctk.CTkLabel(self, text='0', width=260, height=50, font=('Arial', 30), anchor='e')
        self.conteudo.grid(row=0, column=0, padx=10, pady=10)
        

class TecladoNumerico(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        #--> Caracteristicas dos botoes <--
        
        #dimensoes dos botoes (px)
        ALTURA = 70
        LARGURA = 60

        #fonte dos botoes e seu tamanho
        FONTE = 'Arial'
        SIZE = 30

        self.botao_virgula = ctk.CTkButton(self, text=',', height=ALTURA, width=LARGURA, command=lambda:master.input('.'), font=(FONTE, SIZE))
        self.botao_virgula.grid(row=3, column=0, padx=5, pady=5)

        self.botao_zero = ctk.CTkButton(self, text='0', height=ALTURA, width=LARGURA, command=lambda:master.input('0'), font=(FONTE, SIZE))
        self.botao_zero.grid(row=3, column=1, padx=5, pady=5)

        self.botao_igual = ctk.CTkButton(self, text='=', height=ALTURA, width=LARGURA, command=lambda:master.igual(), font=(FONTE, SIZE))
        self.botao_igual.grid(row=3, column=2, padx=5, pady=5)

        self.botao_subtrair = ctk.CTkButton(self, text='-', height=ALTURA, width=LARGURA, command=lambda:master.operation('subtrair'), font=(FONTE, SIZE))
        self.botao_subtrair.grid(row=3, column=3, padx=5, pady=5)

        self.botao_um = ctk.CTkButton(self, text='1', height=ALTURA, width=LARGURA, command=lambda:master.input('1'), font=(FONTE, SIZE))
        self.botao_um.grid(row=2, column=0, padx=5, pady=5)

        self.botao_dois = ctk.CTkButton(self, text='2', height=ALTURA, width=LARGURA, command=lambda:master.input('2'), font=(FONTE, SIZE))
        self.botao_dois.grid(row=2, column=1, padx=5, pady=5)
        
        self.botao_tres = ctk.CTkButton(self, text='3', height=ALTURA, width=LARGURA, command=lambda:master.input('3'), font=(FONTE, SIZE))
        self.botao_tres.grid(row=2, column=2, padx=5, pady=5)

        self.botao_somar = ctk.CTkButton(self, text='+', height=ALTURA, width=LARGURA, command=lambda:master.operation('somar'), font=(FONTE, SIZE))
        self.botao_somar.grid(row=2, column=3, padx=5, pady=5)

        self.botao_quatro = ctk.CTkButton(self, text='4', height=ALTURA, width=LARGURA, command=lambda:master.input('4'), font=(FONTE, SIZE))
        self.botao_quatro.grid(row=1, column=0, padx=5, pady=5)

        self.botao_cinco = ctk.CTkButton(self, text='5', height=ALTURA, width=LARGURA, command=lambda:master.input('5'), font=(FONTE, SIZE))
        self.botao_cinco.grid(row=1, column=1, padx=5, pady=5)

        self.botao_seis = ctk.CTkButton(self, text='6', height=ALTURA, width=LARGURA, command=lambda:master.input('6'), font=(FONTE, SIZE))
        self.botao_seis.grid(row=1, column=2, padx=5, pady=5)

        self.botao_dividir = ctk.CTkButton(self, text='/', height=ALTURA, width=LARGURA, command=lambda:master.operation('dividir'), font=(FONTE, SIZE))
        self.botao_dividir.grid(row=1, column=3, padx=5, pady=5)

        self.botao_sete = ctk.CTkButton(self, text='7', height=ALTURA, width=LARGURA, command=lambda:master.input('7'), font=(FONTE, SIZE))
        self.botao_sete.grid(row=0, column=0, padx=5, pady=5)

        self.botao_oito = ctk.CTkButton(self, text='8', height=ALTURA, width=LARGURA, command=lambda:master.input('8'), font=(FONTE, SIZE))
        self.botao_oito.grid(row=0, column=1, padx=5, pady=5)

        self.botao_nove = ctk.CTkButton(self, text='9', height=ALTURA, width=LARGURA, command=lambda:master.input('9'), font=(FONTE, SIZE))
        self.botao_nove.grid(row=0, column=2, padx=5, pady=5)

        self.botao_multiplicar = ctk.CTkButton(self, text='*', height=ALTURA, width=LARGURA, command=lambda:master.operation('multiplicar'), font=(FONTE, SIZE))
        self.botao_multiplicar.grid(row=0, column=3, padx=5, pady=5)     


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Calculadora')
        self.geometry('300x415')
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)

        self.screen = Screen(self)
        self.screen.grid(row=0, column=0, padx=5, pady=5)

        self.teclado_numerico = TecladoNumerico(self)
        self.teclado_numerico.grid(row=1, column=0, padx=5, pady=5)


    def input(self, string):
        global valor_1, valor_2, entrada

        if entrada:
            valor_1 += string
            self.screen.conteudo.configure(text=valor_1)
        else:
            valor_2 += string
            self.screen.conteudo.configure(text=valor_2)


    def operation(self, string):
        global operacao, entrada, resultado, valor_1

        operacao = string
        entrada = False

        if resultado != 0 and valor_1 == '':
            valor_1 = str(resultado)


    def igual(self):
        global valor_1, valor_2, entrada, resultado, decimal, casas

        if operacao == 'somar':
            resultado = float(valor_1) + float(valor_2)
        elif operacao == 'subtrair':
            resultado = float(valor_1) - float(valor_2)
        elif operacao == 'dividir':
            resultado = float(valor_1) / float(valor_2)
        elif operacao == 'multiplicar':
            resultado = float(valor_1) * float(valor_2)

        self.screen.conteudo.configure(text=f'{resultado}')
        valor_1 = valor_2 = ''
        entrada = True
        

app = App()
app.mainloop()
