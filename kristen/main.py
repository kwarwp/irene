# irene.kristen.main.py
"""Planejamento do jogo da Genética JAIE19
"""
__author__ = "Samuel Novaes Sena"
__version__ = "19.11.11"
from _spy.vitollino.main import STYLE, Cena, Elemento, Texto
STYLE.update(width=850, height="650px") # Atualiza o tamanho da tela

class FioCruz:
    """ Cenário da FioCruz. """
    def __init__(self):
        self.fiocruz = None

    def inicia(self):
        """O jogo inicia aqui. O cenário principal será apresentado """
        self.fiocruz = None

if __name__ == "__main__":
    fc = FioCruz()
    fc.inicia()