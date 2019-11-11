# irene.naomi.main.py
"""Planejamento do jogo da Genética JAIE19
"""
__author__ = "<O seu nome aqui>"
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
        self.ajuda = Elemento(FOCO, x=0, y=350, cena=self.fiocruz,
             style={"opacity": 0},vai=self._ajuda)

    def _ajuda(self, _=0):
        """O personagem dá uma explicação de como encrontrar o lab """
        Texto(self.fiocruz, "O laboratório? Siga pela esquerda").vai()

    def inicia(self):
        """O jogo inicia aqui. O cenário principal será apresentado """
        self.fiocruz.vai()
        Texto(self.fiocruz, "Temos que achar o lab. Vamos perguntar a alguém").vai()


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
        self.ajuda = Elemento(FOCO, x=130, y=100, cena=self.lab,
             style={"opacity": 0},vai=self._ajuda)
        self.denise = Elemento(FOCO, x=260, y=140, cena=self.lab,
             style={"opacity": 0})
        self.caneca = Elemento(CANECA, x=740, y=-200, cena=self.lab,
             style={"opacity": 1})

    def _ajuda(self, _=0):
        """O personagem dá uma explicação de como encrontrar fórmula """
        self.ajuda.vai = self._ajuda5_1
        Texto(self.lab, "A fórmula, tem a ver com 4-4? daqui a pouco lembro mais").vai()

    def _ajuda5_1(self, _=0):
        """O personagem dá uma nova explicação de como encrontrar o lab """
        self.denise.vai = self._ajuda3_2
        Texto(self.lab, "Lembrei! tem 5-1? A denise deve saber mais").vai()

    def _ajuda3_2(self, _=0):
        """O personagem dá uma nova explicação de como encrontrar o lab """
        Texto(self.lab, "O professor me falou o código 3-2? Ele gostava d....").vai()
        
    def inicia(self):
        """O jogo inicia aqui. O laboratório será apresentado """
        self.lab.vai()
        Texto(self.lab, "Temos que achar a fórmula. Vamos perguntar a alguém").vai()


if __name__ == "__main__":
    fc = LembrarHerdeitariedade() #FioCruz()
    fc.inicia()
    
#####################################################################################################

class EntenderHerdeitariedade:
    """Meu caro e querido aprendiz Damon, as informações que você precisa sobre HEREDITARIEDADE
    estão em um pen drive que deixei na gaveta da minha mesa que tem o fundo falso, abra essa geveta
    e pegue esse pen drive, mas lembre-se de que tem pessoas interessadas em roubar a fórmula, por isso
    o pen drive possui uma senha que você terá que ser desvendada através da tabela que você usou
    para descobrir a senha do cofre. A senha tem os seguintes números: 4-4, 5-5, 3-3, 5-1, 2-1, 5-5, 2-2
    
    Imagens: cena lab, cofre, pendrive, tabela
    """    

