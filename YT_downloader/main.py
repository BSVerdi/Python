'''
    Youtube song downloader mp4
    Este codigo possui apenas intuitos educacionais.
    Não utilize de maneira indecente
    Abs: Breno Verdi
'''

import yt_dlp
import customtkinter
from selenium import webdriver
from pathlib import Path
from threading import Thread


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Youtube Downloader")
        self.geometry("400x220")
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")

        self.start_button = customtkinter.CTkButton(self, text="Abrir o YouTube", command=self.iniciar, font = ('Arial', 20), width=300, height=40)
        self.start_button.pack(pady=20)

        self.baixar_button = customtkinter.CTkButton(self, text="Baixar", command=self.startDownload, font = ('Arial', 20), width=300, height=40)
        self.baixar_button.pack(pady=20)

        self.progress_status = customtkinter.CTkLabel(self, text='', font = ('Arial', 20))
        self.progress_status.pack(pady=10)
    

    def iniciar(self):
        self.navegador = webdriver.Chrome()
        self.navegador.set_window_size(1280, 720)
        self.navegador.get('https://www.youtube.com/')


    def startDownload(self):
        Thread(target=self.download).start()


    def download(self):
        def progressBar(d):
            if d['status'] == 'finished':
                self.progress_status.configure(text='Download concluído!')
            else:                
                self.progress_status.configure(text='Baixando!')

        link = self.navegador.current_url
        self.progress_status.configure(text='')

        opcoes = {
            'progress_hooks': [progressBar],
            'format': 'bestaudio[ext=mp4]',
            'outtmpl': f'{(Path.home() / "Desktop/Musicas")}/%(title)s.%(ext)s',  
            'postprocessors': [], 
        }


        with yt_dlp.YoutubeDL(opcoes) as ydl:
            try:
                ydl.download([link])
            except Exception as erro:
                self.progress_status.configure(text=f'Erro: {erro}')


app = App()
app.mainloop()
