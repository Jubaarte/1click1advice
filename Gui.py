import customtkinter as ctk
from tkinter import *
from Aplicacao import App


def time():
    App.relogio(App)
    textohora.configure(text=App.horario)
    textohora.after(1000, time)


def mostrar():
    inicioframe.destroy()
    iniciar.destroy()
    textoconselho.place(relx= 0.5, y=40, anchor= "center")
    textohora.place(x=640, y=260)
    buscarconselho.place(relx=0.5, y=200, anchor="center")

    pass

def aconselhar():
    App.aconselhar(App)
    textoconselho.configure(text=App.conselhoptbr)

    pass


janela = ctk.CTk()
janela.iconbitmap("_internal\\note.ico")
janela.geometry("756x294")
janela.config(background="#FFFDCD")
janela.resizable(width=0, height=0)
janela.title("Adoce sua vida")

inicioframe = ctk.CTkFrame(janela, width=756, height=294, bg_color="#FFFDCD", fg_color="#FFFDCD")
inicioframe.place(x=5, y=5)

textoconselho = ctk.CTkLabel(janela, text="", font=("Robot", 14, "bold"), fg_color="#FFFDCD", bg_color="#FFFDCD", text_color="black", height=100, width=600)

textohora = ctk.CTkLabel(janela, text="", font=("Robot", 16), fg_color="#FFFDCD", bg_color="#FFFDCD", text_color="black")

buscarconselho = ctk.CTkButton(janela, text="BUSCAR CONSELHO", font=("Robot", 24, "bold"), fg_color="#FFFDCD", bg_color="#FFFDCD", text_color="black", hover_color="#fffcb3", command=aconselhar)

iniciar = ctk.CTkButton(janela, text="INICIAR", font=("Robot", 24, "bold"), fg_color="#FFFDCD", bg_color="#FFFDCD", text_color="black", hover_color="#fffcb3", command=mostrar)
iniciar.place(relx=0.5, y=200, anchor="center")


time()

janela.mainloop()
