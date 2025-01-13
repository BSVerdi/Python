import customtkinter as ctk

class Media(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=480, height=100)

        self.grid_columnconfigure((0), weight=1)

        #-> time bar <-

        self.tempo_atual = ctk.CTkLabel(self, text='00:00')
        self.tempo_atual.grid(row=0, column=0, pady=5, padx=5)

        self.progress = ctk.CTkProgressBar(self, width=380)
        self.progress.grid(row=0, column=1, pady=5, padx=5)

        self.tempo_total = ctk.CTkLabel(self, text='05:12')
        self.tempo_total.grid(row=0, column=2, pady=5, padx=10)
         
        self.botao_musica_anterior = ctk.CTkButton(self, width=60, height=60, text='', corner_radius=30)
        self.botao_musica_anterior.grid(row=1, column=0, pady=5, padx=5)

        self.botao_pause = ctk.CTkButton(self, width=60, height=60, text='', corner_radius=30)
        self.botao_pause.grid(row=1, column=1, pady=5, padx=5)

        self.botao_proxima_musica = ctk.CTkButton(self, width=60, height=60, text='', corner_radius=30)
        self.botao_proxima_musica.grid(row=1, column=2, pady=5, padx=5)


class Playlist(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=480, height=380)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Song Player')
        self.geometry('500x500')
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)

        media = Media(self)
        media.grid(row=1, column=0, padx=5, pady=5)

        playlist = Playlist(self)
        playlist.grid(row=0, column=0, padx=5, pady=5)


app = App()
app.mainloop()