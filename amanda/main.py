# irene.amanda.main.py
"""Planejamento do jogo da Genética JAIE19
"""
__author__ = "<O seu nome aqui>"
__version__ = "19.11.11"
from _spy.vitollino.main import STYLE, Cena, Elemento, Texto
STYLE.update(width=850, height="650px") # Atualiza o tamanho da tela
FOCO = "https://i.imgur.com/6e096Va.png"
FIOCRUZ = "https://i.imgur.com/pJDyRCt.jpg"
FREDERICK = "https://i.imgur.com/4EtsjiX.jpg"
QUADRO = "https://i.imgur.com/b2TqQsA.png"
FIOFRONT = "https://i.imgur.com/wdwjGCt.jpg"
AJUDA = "https://i.imgur.com/510Q3z4.png"
FREDERICK = "https://i.imgur.com/4EtsjiX.jpg" #"https://i.imgur.com/377duSy.jpg"
FOCO = "https://i.imgur.com/6e096Va.png"
TABELA = "https://imgur.com/sotDlmO.png"
FIOCRUZ = "https://i.imgur.com/pJDyRCt.jpg"
BIBLIOTECA = "https://i.imgur.com/e6Oc9xU.jpg"
COFRE = "https://i.imgur.com/obMPIpB.png"
PENDRIVE = "https://i.imgur.com/18dBApo.png"
CANECA ="https://i.imgur.com/El0wysJ.png"
TUBO_DE_ENSAIO = "https://www.prolab.com.br/wp-content/uploads/2014/10/1-Tubosdeensaio.jpg"
RELOGIO = "https://i.imgur.com/mevUdpA.png"
QUADRO = "https://i.imgur.com/b2TqQsA.png"
microscopio = "https://i.imgur.com/q414omp.png"
GAVETA = "https://i.imgur.com/85Cta7F.jpg"
ESCRITORIO = "https://i.imgur.com/7zvQ6PZ.jpg"
COFREABERTO = "https://i.imgur.com/mgL4Gp2.png"
TECLACOFRE = "https://i.imgur.com/9NiaFGL.png"

class FioCruz:
    """ Cenário da FioCruz. """
    def __init__(self):
        self.fiocruz = Cena(FIOCRUZ)
        self.ajuda = Elemento(FOCO, x=30, y=350, cena=self.fiocruz, style={"opacity": 0},vai=self._ajuda)
        
    def _ajuda(self, _=0):
        """O personagem dá uma explicação de como encrontrar o lab """
        self.fiocruz.direita = LembrarHerdeitariedade()
        Texto(self.fiocruz, "O laboratório? Siga pela direita").vai()

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
        self.ajuda = Elemento(FOCO, x=130, y=100, cena=self.lab, style={"opacity": 0},vai=self._ajuda)
        self.denise = Elemento(FOCO, x=260, y=140, cena=self.lab, style={"opacity": 0})
        self.quadro = Elemento(QUADRO, x=422, y=140, cena=self.lab, vai=self._ajuda25_1)
        self.maria = Elemento(FOCO, x=635, y=160, cena=self.lab, style={"opacity": 0},vai=self._ajuda2_2)
        self.joana = Elemento(FOCO, x=770, y=150, cena=self.lab, style={"opacity": 0},vai=self._ajudajoana)
        self.tabela = Elemento(TABELA, x=222, y=100, cena=self.lab, vai=self._ajudatabela)
        
    def _ajuda(self, _=0):
        """O personagem dá uma explicação de como encontrar formula """
        self.ajuda.vai = self._ajuda5_1
        Texto(self.lab, "A fórmula ? Tem a ver com 4-4. Daqui a pouco lembro mais.").vai()

    def _ajuda5_1(self, _=0):
        """O personagem dá uma explicação de como encontrar a formula """ 
        self.denise.vai = self._ajuda3_2
        Texto(self.lab, "Lembrei ! Tem 5-1. A Denise deve saber mais").vai()
        
    def _ajuda3_2(self, _=0):
        """O personagem dá uma explicação de como encontrar a formula """
        self.quadro.vai = self._ajuda25_1
        Texto(self.lab, "Denise: O professor me falou o código 3-2. Ele gostava muito de rabiscar no quadro").vai()
        
        
    def _ajuda25_1(self, _=0):
        """O personagem dá uma explicação de como encontrar a formula """
        Texto(self.lab, "Olha só o código 5-1 ! Tem também um nome... Maria").vai()
        
    def _ajuda2_2(self, _=0):
        """O personagem dá uma explicação de como encontrar a formula """
        Texto(self.lab, "Maria: Ele só me falava da importancia de duas pessoas ficarem juntas. Como ele sempre fez aqui no laboratório, ficavamos sempre em duplas. Será o que isso significa ? Não consigo entender se isso é um código... O que voce pensa Joana ?").vai()
    
    def _ajudajoana(self, _=0):
        """O personagem dá uma explicação de como encontrar a formula """
        Texto(self.lab, "Joana: Tão inteligente para umas coisas... Maria, é claro que o código é 2-2. Vejam lá na tabela que está na bancada o que isto significa").vai()

    def _ajudatabela(self, _=0):
        """O personagem dá uma explicação de como encontrar a formula """
        Texto(self.lab, "O que significa esta sequencia ? 4-4, 5-1, 3-2, 5-1, 2-2 ? Vamos ver se a tabela ajuda").vai()
        
    def inicia(self):
        """O jogo inicia aqui. O cenário principal será apresentado """
        self.lab.vai()
        Texto(self.lab, "Temos que achar a fórmula. Vamos perguntar a alguém").vai()

    def vai(self):
        """O jogo inicia aqui. O cenário principal será apresentado """
        self.lab.vai()
        Texto(self.lab, "Temos que achar a fórmula. Vamos perguntar a alguém").vai()
        
if __name__ == "__main__":
    #fc = LembrarHerdeitariedade() #FioCruz()
    fc = FioCruz()
    fc.inicia()