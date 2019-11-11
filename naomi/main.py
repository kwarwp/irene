# irene.naomi.main.py
"""Planejamento do jogo da Genética JAIE19
"""
__author__ = "<O seu nome aqui>"
__version__ = "19.11.11"
from _spy.vitollino.main import STYLE, Cena, Elemento, Texto
STYLE.update(width=850, height="650px") # Atualiza o tamanho da tela
FOCO = "https://i.imgur.com/6e096Va.png"
FIOCRUZ = "https://i.imgur.com/pJDyRCt.jpg"
FREDERICK = "https://i.imgur.com/4EtsjiX.jpg"
CANECA ="https://i.imgur.com/El0wysJ.png"

class FioCruz:
    """ Cenário da FioCruz. """
    def __init__(self):
        self.fiocruz = Cena(FIOCRUZ)
        self.ajuda = Elemento(FOCO, x=0, y=350, cena=self.fiocruz,
             style={"opacity": 0},vai=self._ajuda)

    def _ajuda(self, _=0):
        """O personagem dá uma explicação de como encrontrar o lab """
        Texto(self.fiocruz, "O laboratório? Siga pela esquerda").vai()

    def inicia(self):
        """O jogo inicia aqui. O cenário principal será apresentado """
        self.fiocruz.vai()
        Texto(self.fiocruz, "Temos que achar o lab. Vamos perguntar a alguém").vai()
    
    def ajuda(self, _=0):
    """ O personagem dá uma explicação de como encontrar o la"""
        Texto=(self.fiocruz, "O laboratório? Pela esquerda.").vai()
        
        
        if __name__ == "__main__":
    fc = FioCruz()
    fc.inicia()



