# irene.kathryn.main.py
"""Planejamento do jogo da Genética JAIE19
"""
__author__ = "<Vania Sara>"
__version__ = "19.11.11"
from _spy.vitollino.main import STYLE, Cena, Elemento, Texto
STYLE.update(width=850, height="650px") # Atualiza o tamanho da tela
FOCO = "http://i.imgur.com/6e096Va.png"
FIOCRUZ = "http://i.imgur.com/pJDyRCt.jpg"


class FioCruz:
    """ Cenário da FioCruz. """
    def __init__(self):
        self.fiocruz = Cena(FIOCRUZ)
        self.ajuda = Elemento(FOCO, x= 30, y=300, cena=self.fiocruz)
        
    def inicia(self, =0):
        """O personagem dá uma explicação de como encontrar o lab"""
        Texto(self.fiocruz, "O laboratório?Siga pela esquerda").vai()
        
    def inicia(self):
        """O jogo inicia aqui. O cenário principal será apresentado """
        self.fiocruz.vai()
        Texto(self.fiocruz, "Temos que achar o lab. Vamos perguntar a alguém").vai()

if __name__ == "__main__":
    fc = FioCruz()
    fc.inicia()
