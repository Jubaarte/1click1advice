



![image](https://github.com/Jubaarte/1click1advice/assets/113859220/f237eb43-d9d2-46aa-9cf4-3b7415ce7d17)  ![image](https://github.com/Jubaarte/1click1advice/assets/113859220/522fbbb7-4688-462f-952c-5a8af2472329)


# One click - One advice



**This is my first project as a non-progammer and it is done in python.**



The App has been splitted into two files, one for interface manipulation and the other for only functions.

It begins using the "**customtkinter**" library to build a window and for design it.

```
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

```

After all labels and buttons has been built, i focused on the function code. Using **Advice Slip JSON API** and "**requests**" library i made a function that requests __"https://api.adviceslip.com/advice"__ info and store it in a *var*. Then, using "**json**" library i convert the info stored into a single json data and use it to extract the text inside it, which is a random advice provided by the _API_.

Once i have the advice, it is written in English, which is not my language, then, i use the "**deep_translator**" and import "**GoogleTranslator**" to the project so i translate the advice i got previously.

Using the time library i made a simple clock counter that print the time every second. 

```
class App():
    def aconselhar(self):
        tradutor = GoogleTranslator(source= "en", target= "pt")
        info = requests.get("https://api.adviceslip.com/advice")
        info = info.json()
        conselho = info["slip"]["advice"]
        print(conselho)
        self.conselhoptbr = tradutor.translate(conselho)
        print (self.conselhoptbr)

        pass

    def relogio(self):
        hora = time.asctime(time.localtime())
        info = hora.split()
        self.horario = info[3]
        print (self.horario)        
        

```


After made all the working functions i went to the interface file and imported them, making it works with interface's button and labels.


--------------------
**References**
```
import customtkinter as ctk
from tkinter import *
from Aplicacao import App

from deep_translator import GoogleTranslator
import time
import requests
import json
```

- customtkinter
- deep_translator - GoogleTranslator
- API - Advice slip JSON API
- requests
- json
