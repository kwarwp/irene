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
        self.ajuda = Elemento(FOCO, x=70, y=400, w=50, h=50, cena=self.fiocruz, style={"opacity": 0.3}, vai=self._ajuda)
        self.irProLab = Elemento(FOCO, x=570, y=330, cena=self.fiocruz, style={"opacity": 0.3})
	
    def _ajuda(self, _=0):
        """ O personagem dá uma explicação de como encontrar o lab. """
        # self.fiocruz.irProlab.style["opacity"] = 0.3
        self.fiocruz.irProLab = LembrarHerdeitariedade()
        Texto(self.fiocruz, "O laboratório está na direita.").vai()
        
    def _irProLab(self, _=0):
        self.fiocruz.irProlab.inicia()
        
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
        self.denise = Elemento(FOCO, x=280, y=150, cena=self.lab, style={"opacity": 0})
        self.raquel = Elemento(FOCO, x=630, y=180, cena=self.lab, style={"opacity": 0})
        self.amanda = Elemento(FOCO, x=780, y=150, cena=self.lab, style={"opacity": 0})

    def _ajuda(self, _=0):
        """ O personagem dá uma explicação de como encontrar o lab. """
        self.ajuda.vai = self._ajuda5_1
        Texto(self.lab, "A fórmula? Tem a ver com 4-4? Daqui a pouco eu lembro mais.").vai()
        
    def _ajuda5_1(self, _=0):
        """ O personagem dá uma explicação de como encontrar o lab. """
        self.denise.vai = self._ajuda3_2
        self.raquel.vai = self._naoSouDenise
        self.amanda.vai = self._naoSouDenise
        Texto(self.lab, "Ah, lembrei! Tem 5-1? A Denise deve saber mais").vai()
    
    def _naoSouDenise(self, _=0):
        """ Ela diz que não é a denise """
        Texto(self.lab, "A Denise está do outro lado.").vai()
        
    def _ajuda3_2(self, _=0):
        """ A Denise dá uma explicação de como encontrar o lab. """
        self.amanda.vai = self._ajuda2_2
        self.raquel.vai = self._raquel
        Texto(self.lab, "O código que você precisa é o 3-2. Talvez a Amanda, que está do outro lado, saiba mais...").vai()
        
    def _raquel(self, _=0):
        """ A Raquel diz que não é a Amanda. """
        Texto(self.lab, "Eu sou a Raquel. A Raquel é a moça do meu lado.").vai()
        
    def _ajuda2_2(self, _=0):
        """ A Amanda diz a última pista """
        Texto(self.lab, "O último código para você decifrar a palavra-chave é 2-2.").vai()
    
    def inicia(self, _=0):
        """ Muada para o laboratório """
        self.lab.vai()
        Texto(self.lab, "Temos que achar a fórmula. Vamos perguntar à alguem").vai()
        
if __name__ == "__main__":
    fc = FioCruz()
    fc.inicia()
#####################################################################################################