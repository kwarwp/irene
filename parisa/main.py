# irene.roxanne.main.py

"""Planejamento do jogo da Genética JAIE19
"""
__author__ = "<Oto Assunção - oto.braz@outlook.com>"
__version__ = "19.11.11"

from _spy.vitollino.main import STYLE, Cena, Elemento, Texto
STYLE.update(width=850, height="650px") # Atualiza o tamanho da tela

FOCO = "https://i.imgur.com/6e096Va.png"
FIOCRUZ = "https://i.imgur.com/pJDyRCt.jpg"
FREDERICK = "https://i.imgur.com/4EtsjiX.jpg"

class FioCruz:
    """ Cenário da FioCruz. """
    def __init__(self):
        self.fiocruz = Cena(FIOCRUZ)
        self.ajuda = Elemento(FOCO, x=30, y=350, cena=self.fiocruz, style={"opacity": 0.5}, vai=self._ajuda)
        self.irProLab = Elemento(FOCO, x=800, y=600, cena=self.fiocruz, style={"opacity": 0}, vai=self._irProLab)
	
    def _ajuda(self, _=0):
        """ O personagem dá uma explicação de como encontrar o lab. """
        Texto(self.fiocruz, "O laboratório está na direita.").vai()
    
    def _irProLab(self, _=0):
        """ Muda para o cenário do laboratório """
        lab = LembrarHerdeitariedade()
        lab.inicia()
        
    def inicia(self):
        """O jogo inicia aqui. O cenário principal será apresentado """
        self.fiocruz.vai()
        Texto(self.fiocruz, "Temos que achar o laboratório. Talvez alguem aqui saiba onde é.").vai()

class LembrarHerdeitariedade:
    """Após a morte do cientista Frederick, planejavam roubar sua fórmula em seu laboratório,
    seu fiel amigo e aprendiz Damon, precisa procurar a fórmula para protegê-la que está no laboratório,
    porém seu amigo antes de morrer disse-lhe "botei a fórmula dentro deste cofre, cujo a senha é formada
    por letras, que estão espalhadas em meu laboratório.". Existe uma tabela deixada pelo cientitsa para
    decifrar quais letras formam a palavra-chave (4-4, 5-1, 3-2, 5-1, 2-2= GENES). 
    
    Imagens: cena lab, caneca, tubo de ensaio, relógio, quadro, microscópio
    Na verdade, adaptei para perguntar a pessoas que já estavam na cena
    """
    
    def __init__(self):
        self.lab = Cena(FREDERICK)
        self.ajuda = Elemento(FOCO, x=120, y=80, cena=self.lab, style={"opacity": 0}, vai=self._ajuda)
        self.denise = Elemento(FOCO, x=230, y=80, cena=self.lab, style={"opacity": 1})
	
    def _ajuda(self, _=0):
        """ O personagem dá uma explicação de como encontrar o lab. """
        Texto(self.lab, "A fórmula? Tem a ver com 4-4? Daqui a pouco eu lembro mais.").vai()
        
    def _ajuda3_1(self, _=0):
        """ O personagem dá uma explicação de como encontrar o lab. """
        self.ajuda.vai = self.ajuda_3_1
        Texto(self.lab, "Ah, lembrei! Tem 5-1? A denise deve saber mais").vai()
        
    def _ajuda3_2(self, _=0):
        """ A Denise dá uma explicação de como encontrar o lab. """
        Texto(self.lab, "O código que você precisa é o 3-2.").vai()
    
    def inicia(self):
        """ Muada para o laboratório """
        self.lab.vai()
        Texto(self.lab, "Temos que achar a fórmula. Vamos perguntar à alguem").vai()
        
if __name__ == "__main__":
    fc = LembrarHerdeitariedade()
    fc.inicia()
#####################################################################################################