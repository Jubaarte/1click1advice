from deep_translator import GoogleTranslator
import time
import requests
import json


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
        

