# irene.ruzwana.main.py
"""Planejamento do jogo da Genética JAIE19
"""
__author__ = "Gabriel"
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
        self.ajuda = Elemento(FOCO,x=0,y=350, cena=self.fiocruz, style={"opacity": 0}, vai=self._ajuda)

    def _ajuda(self, _=0):
        """O personagem dá uma explicação de como encontrar o laboratório """
        self.fiocruz.direita = LembrarHerdeitariedade()
        Texto(self.fiocruz, "O laboratório? Siga pela direita").vai()
        
    def inicia(self):
        """O jogo inicia aqui. O cenário principal será apresentado """
        self.fiocruz.vai()
        Texto(self.fiocruz,"Temos que achar o laboratório. vamos perguntar a alguém").vai()

class LembrarHereditariedade:
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
        self.ajuda = Elemento(FOCO,x=130,y=100, cena=self.lab, style={"opacity": 1}, vai=self._ajuda)
        self.denise = Elemento(FOCO,x=260,y=140, cena=self.lab, style={"opacity": 1})
        self.caneca = Elemento(CANECA,x=740,y=480, cena=self.lab, style={"opacity": 1})


    def _ajuda(self, _=0):
        """O personagem dá uma explicação de como encontrar o laboratório """
        self.ajuda.vai=self._ajuda5_1
        Texto(self.lab,"A fórmula tem a ver com 4-4? Daqui a pouco lembro mais.").vai()

    def _ajuda5_1(self, _=0):
        """O personagem dá uma explicação de como encontrar o laboratório """
        self.denise.vai = self._ajuda3_2
        Texto(self.lab,"Lembrei! Tem 5-1? A Denise deve saber mais").vai()

    def _ajuda3_2(self, _=0):
        """O personagem dá uma explicação de como encontrar o laboratório """
        self.caneca.vai = self.caneca_dica
        Texto(self.lab,"O professor me falou o código 3-2? Ele gostava de café").vai()

    def caneca_dica(self, _=0):
        """O personagem dá uma explicação de como encontrar o laboratório """
        Texto(self.lab,"Achou!").vai()

    def vai(self):
        """O jogo inicia aqui. O laboratório será apresentado """
        self.lab.vai()
        Texto(self.lab, "Temos que achar a fórmula. Vamos perguntar a alguém").vai()

    def inicia(self):
        """O jogo inicia aqui. O cenário principal será apresentado """
        self.lab.vai()
        Texto(self.lab,"Temos que achar a fórmula. vamos perguntar a alguém").vai()

if __name__ == "__main__":
    fc = FioCruz()
    fc.inicia()
#    fc.ajuda()
#    fc = LembrarHereditariedade
#    fc.inicia()