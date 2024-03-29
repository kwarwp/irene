# irene.tracy.main.py
"""Planejamento do jogo da Genética JAIE19
"""
__author__ = "<VaniaSara>"
__version__ = "19.11.11"
from _spy.vitollino.main import STYLE, Cena, Elemento, Texto
STYLE.update(width=850, height="650px") # Atualiza o tamanho da tela
FOCO = "https://i.imgur.com/6e096Va.png"
FIOCRUZ = "https://i.imgur.com/pJDyRCt.jpg"

class FioCruz:
    """ Cenário da FioCruz. """
    def __init__(self):
        self.fiocruz = Cena(FIOCRUZ)
        self.ajuda=Elemento(FOCO, x= 30, y=350, cena=self.fiocruz, vai=self.ajuda)

    def ajuda(self=0, _=0):
        """O personagem da uma explicação de como encontrar o laboratório """
        self.fiocruz.vai()
        Texto(self.fiocruz, "O laboratório? Siga pela esquerda").vai()

    def inicia(self):
        """O jogo inicia aqui. O cenário principal será apresentado """
        self.fiocruz.vai()
        Texto(self.fiocruz, "Temos que achar o laboratório. Vamos perguntar a alguém").vai()

if __name__ == "__main__":
    fc = FioCruz()
    fc.inicia()