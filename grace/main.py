# irene.grace.main.py
"""Planejamento do jogo da Genética JAIE19
"""
__author__ = "Carlo E T Oliveira"
__version__ = "19.11.05"
from _spy.vitollino.main import STYLE, Cena, Elemento, Texto
STYLE.update(width=850, height="650px")
FIOFRONT = "https://i.imgur.com/wdwjGCt.jpg"
AJUDA = "https://i.imgur.com/510Q3z4.png"

class FioCruz:
    """ Cenário da FioCruz. """
    def __init__(self):
        self.fc = Cena(FIOFRONT, direita=self, meio=self, esquerda=self)
        self.ajuda = Elemento(AJUDA, x=470, y=510, w=300, h=40, cena=self.fc)
        self.ajuda.elt.style.opacity = 0
        
    def vai(self, *_):
        Texto(self.fc, "Você chegou na FioCruz, procure alguem para te ajudar").vai()
        self.ajuda.vai = self.ajudar
        
    def ajudar(self, *_):
        Texto(self.fc, "Siga pela direita para entrar no lab").vai()
        self.fc.direita = Texto(self.fc, "ok você vai chegar lá")
        
        
    def inicia(self):
        self.fc.vai()

class E:
    """Meu caro e querido aprendiz Damon, as informações que você precisa sobre HEREDITARIEDADE
    estão em um pen drive que deixei na gaveta da minha mesa que tem o fundo falso, abra essa geveta
    e pegue esse pen drive, mas lembre-se que tem pessoas interessadas em roubar a fórmula, por isso
    o pen drive possui uma senha que você terá que ser desvendada através da tabela que você usou
    para descobrir a senha do cofre. A senha tem os seguintes números: 4-4, 5-5, 3-3, 5-1, 2-1, 5-5, 2-2
    
    Imagens: cena lab, cofre, pendrive, tabela
    """    
def grace():
    fc = FioCruz()
    fc.inicia()
    
    
if __name__ == "__main__":
    grace()