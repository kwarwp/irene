# irene.alexa.main.py
"""Planejamento do jogo da Genética JAIE19
"""
__author__ = "Tarcísio Hazin"
__version__ = "19.11.11"
from _spy.vitollino.main import STYLE, Cena, Elemento, Texto
STYLE.update(width=850, height="650px") # Atualiza o tamanho da tela

"""Assets"""
FOCO = "https://i.imgur.com/6e096Va.png"
FIOCRUZ = "https://i.imgur.com/pJDyRCt.jpg"

class FioCruz:
    """ Cenário da FioCruz. """
    def __init__(self):
        self.fiocruz = Cena(FIOCRUZ)
        self.dica_inicial = Elemento(FOCO, x=50, y=400, cena=self.fiocruz, 
            style={"opacity": 0.1}, vai=self.ajuda_personagem)

    def ajuda_personagem(self, _=0):
        """O personagem dará uma dica de como encontrar o lab."""
        Texto(self.fiocruz, "Para encontrar o lab, você precisa seguir para esquerda...").vai()
        

    def inicia(self):
        """O jogo inicia aqui. O cenário principal será apresentado """
        self.fiocruz.vai()
        Texto(self.fiocruz, "Precisamos encontrar o lab. Quem tem boca vai a Roma!").vai()


if __name__ == "__main__":
    fc = FioCruz()
    fc.inicia()
#####################################################################################################