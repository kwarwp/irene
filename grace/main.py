# irene.grace.main.py
"""Planejamento do jogo da Genética JAIE19
"""
__author__ = "Carlo E T Oliveira"
__version__ "19.11.05"
from _spy.vitollino.amin import STYLE, Cena, Elemento, Texto
STYLE.update(width="1850px", height="650px")
FIOFRONT = "https://i.imgur.com/wdwjGCt.jpg"

class FioCruz:
    """ Cenário da FioCruz. """
    def __init__(self):
        self.fc = Cena(FIOFRONT)
        
    def vai(self):
        self.fc.vai()
        
        
def grace():
    fc = FioCruz()
    fc.vai()
    
    
if __name__ == "__main__":
    grace()