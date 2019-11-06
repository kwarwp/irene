# irene.danae.main.py
"""
Uma expedição para coletar os tesouros do Templo Inca
 --Relato:
 fui e voltei rico
"""
__author__ = "Carlo E T Oliveira <carlo at nce ufrj br>"
__version__ = "19.11.06"
from random import randint
from collections import defaultdict


class Explorador:
    """ explora o templo inca"""
    def __init__(self):  # (self, camara)
        self.mochila = 0
        self.cabana = 0
        # self.camara = camara?
            
    def pega(self, quantidade, camara):
        """ coloca um tesouro na mochila """
        print(f"Você coloca {quantidade} tesouro na mochila ")
        self.mochila += quantidade
        print(f"Você fica com {self.mochila} tesouros na mochila ")
        camara.entra(self)
                    
    def sai(self):
        """ sai do templo """
        print("Você sai do templo e guarda os tesouros!")
        self.cabana, self.mochila = self.mochila, 0
        print(f"Você ficou com {self.cabana} tesouros na cabana!")


class Camara:
    def __init__(self):
        self.quantidade = 3
        #self.explorador = explorador
        
    def entra(self, explorador):
        """ entra em uma câmara"""
        print()
        if input("Você entra em uma câmara com tesouros! Continua?").lower() == "s":
            if self.quantidade:
                self.quantidade -= 1        
                explorador.pega(randint(1, 4), self)
            else:
                input("Não havia mais tesouros!")
                explorador.sai()
        else:
            return
        


class TemploInca:
    def __init__(self):
        self.explorador = Explorador()
        self.camara = Camara()
        self.decide = defaultdict(lambda: self.desiste)
        self.decide.update(s=self.entra)
        
    def inicia(self):
        """ inicia a exploração """
        self.decide[input("Uma expedição para coletar os tesouros do Templo Inca. Você vai explorar o templo (s/N)?")]()
        
    def desiste(self):
        """ aborta a exploração """
        input("Uma sábia decisão, seria loucura explorar este templo macabro!")
        
    def entra(self):
        """ o explorador decide entrar no templo """
        self.camara.entra(self.explorador)
        
        
    


if __name__ == "__main__":
    TemploInca().inicia()

