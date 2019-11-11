# irene.roxanne.main.py

"""Planejamento do jogo da Genética JAIE19
"""
__author__ = "<Oto Assunção - oto.braz@outlook.com>"
__version__ = "19.11.11"

from _spy.vitollino.main import STYLE, Cena, Elemento, Texto
STYLE.update(width=850, height="650px") # Atualiza o tamanho da tela

FOCO = "https://i.imgur.com/6e096Va.png"
FIOCRUZ = "https://i.imgur.com/pJDyRCt.jpg"

class FioCruz:
    """ Cenário da FioCruz. """
    def __init__(self):
        self.fiocruz = None

    def inicia(self):
        """O jogo inicia aqui. O cenário principal será apresentado """
        self.fiocruz = FIOCRUZ


if __name__ == "__main__":
    fc = FioCruz()
    fc.inicia()
#####################################################################################################