# irene.grace.main.py
"""Planejamento do jogo da Genética JAIE19

v 19.11.05b - adiciona lembra hereditariedade
"""
__author__ = "Carlo E T Oliveira"
__version__ = "19.11.05b"
from _spy.vitollino.main import STYLE, Cena, Elemento, Texto
from collections import namedtuple
Pista = namedtuple("Pista", "x y dica")
STYLE.update(width=850, height="650px")
FIOFRONT = "https://i.imgur.com/wdwjGCt.jpg"
AJUDA = "https://i.imgur.com/510Q3z4.png"
FREDERICK = "https://i.imgur.com/4EtsjiX.jpg" #"https://i.imgur.com/377duSy.jpg"
FOCO = "https://i.imgur.com/6e096Va.png"
TABELA = "https://imgur.com/sotDlmO.png"

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
        self.fc.direita = LembrarHerdeitariedade() #Texto(self.fc, "ok você vai chegar lá")
        
        
    def inicia(self):
        self.fc.vai()

class EntenderHerdeitariedade:
    """Meu caro e querido aprendiz Damon, as informações que você precisa sobre HEREDITARIEDADE
    estão em um pen drive que deixei na gaveta da minha mesa que tem o fundo falso, abra essa geveta
    e pegue esse pen drive, mas lembre-se que tem pessoas interessadas em roubar a fórmula, por isso
    o pen drive possui uma senha que você terá que ser desvendada através da tabela que você usou
    para descobrir a senha do cofre. A senha tem os seguintes números: 4-4, 5-5, 3-3, 5-1, 2-1, 5-5, 2-2
    
    Imagens: cena lab, cofre, pendrive, tabela
    """    

class LembrarHerdeitariedade:
    """Após a morte do cientista Frederick, planejavam roubar sua fórmula em seu laboratório,
    seu fiel amigo e aprendiz Damon, precisa procurar a fórmula para protegê-la que está no laboratório,
    porém seu amigo antes de morrer disse-lhe "botei a fórmula dentro deste cofre, cujo a senha é formada
    por letras, que estão espalhadas em meu laboratório.". Existe uma tabela deixada pelo cientitsa para
    decifrar quais letras formam a palavra-chave (4-4, 5-1, 3-2, 5-1, 2-2= GENES). 
    
    Imagens: cena lab, caneca, tubo de ensaio, relógio, quadro, microscópio
    """
    def __init__(self):
        self.codigo = [
        Pista(100, 70, "A única parte que sei é algo como 4-4, deixe eu pensar mais"),
        Pista(600, 150, "ah, a fórmula do Dr. Frederick tem 5-1, uma das meninas sabe o resto"),
        Pista(750, 140, "ah, o que você procura tem a ver com 3-2, a Débora deve saber mais"),
        Pista(270, 120, "A Shirley é uma fofoqueira, mas já que ela já falou, posso te contar o 5-1"),
        Pista(400, 450, "A Joana uma vez falou algo como com 2-2, lembro que alguém anotou o resto"),
        Pista(700, 110, "Na verdade, tudo está em uma tabela colada no quadro"),
        Pista(700, 110, "Você pega a tabela colada no quadro"),
        ]
        p = self.codigo[0]
        self.dica = 0
        self.fc = Cena(FREDERICK, direita=self, meio=self, esquerda=self)
        self.ajuda = Elemento(FOCO, x=p.x, y=p.y, w=150, h=150, cena=self.fc,vai=self.pista)
        self.tabela = Elemento(TABELA, x=720, y=130, w=60, h=60, cena=self.fc)
        self.ajuda.elt.style.opacity = 0.5
        self.inicia = self.vai
        
    def pista(self, *_):
        p = self.codigo[self.dica]
        self.dica += 1
        Texto(self.fc, p.dica).vai()
        self.ajuda.elt.style.left = p.x
        self.ajuda.elt.style.top = p.y
        if self.dica > 6 :
            self.tabela.elt.style.left = 170
            self.tabela.elt.style.top = 120
            self.tabela.elt.style.width = 500
            self.tabela.elt.style.width = "500px"
        
    def vai(self, *_):
        self.fc.vai()
        Texto(self.fc, "Você chegou ao lab do Dr.Frederick, procure pistas da fórmula").vai()

def grace():
    fc = FioCruz()
    fc = LembrarHerdeitariedade()
    fc.inicia()
    
    
if __name__ == "__main__":
    grace()