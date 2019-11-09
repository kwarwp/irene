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

#Inicio Jogo 1
class LembraGene:
    """O cientista sobe as escadas da biblioteca, ele encontra porções de sangue entre as prateleiras. 
    Desconfiado ele resolve ir na câmera de vigilância, para tentar reconhecer a pessoa. Mas não consegue. 
    Não há saída! Setas piscam, ilustrando o caminho, o jogador segue, chega a porta, ela se abre, laboratório.
    Imagens soltas na bancada: Fragmento,DNA, Proteína, Molécula, Gene, Átomos, Ordene.
    """
class EntendeGene:
    """Entender-gene: A cientista sai, rola um pedra, cai uma grade, ela está Â´presa, surge um enigma, 
    acerte a charada, ela precisa correr, aparecem palavras desorganizadas. 
    Imagens: Núcleo, Cromossomo +histonas,Proteína
    """
class AplicaGene:
    """A  cientista entra e correlacione os fragmentos corretos. 
    Imagens: Tesouras moleculares, Fragmentos DNA coloridos roxos,Fragmentos DNA preto e branco, 
    Fragmentos de DNA amarelos, Produção de flor colorida roxa
    """
    
class AnalisaGene:
    """A cientista entra.Há um mundo mágico, há personagens mágicos, histonas, fragmentos de DNA
    codificados e nao codificados. A porta se tranca. Surge um "cientista" fantasma. Aparece um 
    relógio gigante e fantasmagórico. Você te xx tempo para formar a proteina xyz, que lhe dará 
    super poderes.Faça as correlações corretas, Forma um líquido brilhoso, Bebe, Adquire super poderes.
    Imagens: DNA codificado, DNA não codificado, Proteína XYZ,Gene KPY, Gene XVZ, Proteína KPI,
    Estabilidade, Faça as correlações corretas, Forma um líquido brilhoso, Bebe, Adquire super poderes.
    """
class AvaliaGene:

    """A cientista entra num calabouço, há uma pessoa presa. Solta a pessoa. Você está fraca, não conseguirá fugir
    Volte na fase anterior. Tome a poção brilhosa sobre a mesa. Gene com super poderes. Cuidado.
    Não sabemas a reação. Há apenas uma passagem. Surgem vários seres.Várias perguntas caem de cima
    Pegue a pergunta. Digite na passagem a resposta correta.Justifique a existência do gene.
    """
class criaGene:
    """A cientista precisa criar a sequência correta para criar uma nova proteína que irá originar o novo ser
    Vários códons.
    AUU - AUG - CGC - AAA - CAV - UGA - AUA - Proteína
    Faça a combinação correta e crie uma nova proteína de um novo ser.
    """
#Fim do jogo 1
    
#inicio jogo 2
class LembrarRNA:
    """ O ajudante do cientista logo após acordar nas escadas próximo ao laboratório observou que hava
    uma garça com coloração diferente das normais, percebeu que era modificada genéticamente.Precisa capturá-la. 
    Há uma rede pendurada na parede,ele pega, joga na graça, aparentemente normal. Captura
    Leva para o laboratório. Pega uma pena, Observa a célula, dentro dela há uma estrutura em formato de fita,
    Ele escuta um barulho! Tenta achar uma passagem, as portas estão trancadas, ele olha a estante, puxa um livro,
    Há um enigma, tecle na combinação correta.
  
   RNA     DNA    CO2

   A        U      C      G

   P        M      N      V

   S        X      Z      O

   """

class EntenderRNA:
    """Chega num jardim da FIOCRUZ, ele se aproxima, uma caixa de música ela se abre, com um holograma  contendo
    uma estrutura.Resultado de imagem para imagem rna composição. Surge uma graça genéticamente modificada, ela 
    é muito grande corre atrás do jogador.
    Ele corre. Passa por um longo corredor. Sai num hospital.Há uma pandemia de marasmo, por toda a cidade
    O jogador precisa curar as pessoas. Surge o NPC- A cura está no holograma apresentado.
    """


class AplicarRNA:
    """Passa pela cidade. Há muitas pessoas doentes. Precisa da produção de um antídoto em larga escala
    Volta para o laboratório. Vai para o microscópio. Observa o núcleo da célula. No núcleo parte brilhante (DNA)
    Pega o fragmento de DNA. Pega uma bactéria. Introduz na bactéria. Reprodução bactérias. Pega o antídoto
    Leva para o hospital principal.Salva as pessoas.
    """
class AnalisarRNA:
    """Vai para o museu da vida, chega lá na bancada há várias moléciulas  de RNA espalhadas na bancada.
    Há funções. O jogador precisa linkar os RNA as funções específicas. 
    Imagens: Tradução, RNAr,RNAt, Transportador, Constituição dos ribossomos, Acelera metabolismo celular
    RNAs, Produção de lipase, Produção de células.
    """

class AvaliarRNA:

    """Caminha para outra sala do museu. Aparece um cientista. Impede sua passagem. 
    Fala com uma voz assombrosa.
    """

class CriarRNA:

    """No laboratório. Abre o computador. Pesquisa como acabar com a tristeza do planeta
    No microscópio observa a célula. Pega o RNA. Acrescenta novos códons. Muda sua forma.
    Produz serotonina.
    """

class EntenderHerdeitariedade:
    """Meu caro e querido aprendiz Damon, as informações que você precisa sobre HEREDITARIEDADE
    estão em um pen drive que deixei na gaveta da minha mesa que tem o fundo falso, abra essa geveta
    e pegue esse pen drive, mas lembre-se que tem pessoas interessadas em roubar a fórmula, por isso
    o pen drive possui uma senha que você terá que ser desvendada através da tabela que você usou
    para descobrir a senha do cofre. A senha tem os seguintes números: 4-4, 5-5, 3-3, 5-1, 2-1, 5-5, 2-2
    
    Imagens: cena lab, cofre, pendrive, tabela
    """    
    def __init__(self):
        self.escritorio()
        #self.abre()
        
    def escritorio(self, *_):
        self.fc = Cena(ESCRITORIO, direita=self, meio=self, esquerda=self)
        self.ajuda = Elemento(COFRE, x=120, y=80, w=250, h=250, cena=self.fc,vai=self.pista)
        self.tabela = Elemento(COFREABERTO, x=720, y=130, w=60, h=60, cena=self.fc)
        # self.ajuda.elt.style.opacity = 0.01
        self.inicia = self.vai
        self.senha = ""
        
    def vai(self, *_):
        self.fc.vai()
        Texto(self.fc, "Você chegou ao escritório do Dr.Frederick, procure pistas da fórmula").vai()
        
    def pista(self, *_):
        self.tecla = Elemento(TECLACOFRE, x=0, y=0, w=850, h=650, cena=self.fc,vai=self.pista)
        style = dict(opacity=0.1)
        self.ks = [Elemento(FOCO, x=80+k%3 *260, y=50+k//3*150, w=190, h=120, style =style,
            cena=self.fc,vai=lambda *_, i=k:self.codigo(str(i+1))) for k in range(9)]
        
    def codigo(self, valor):
        self.senha+=valor
        abriu = ", você abriu o cofre" if self.senha == "43637" else ", mas a senha está errada"
        abre = self.abre if self.senha == "43637" else self.mostra
        if len(self.senha) >4:
            #senha = "".join(self.senha)
            Texto(self.fc, f"Você digitou a senha {self.senha}{abriu}", foi = abre).vai()
        
    def abre(self, *_):
        self.mostra()
        self.aberto = Elemento(COFREABERTO, x=-50, y=-50, w=950, h=750, cena=self.fc)
        self.pendrive = Elemento(PENDRIVE, x=300, y=360, w=150, h=150, cena=self.fc,vai=self.pen)
        
    def mostra(self, *_):
        self.escritorio()
        self.fc.vai()
        
    def pen(self, *_):
        def escritorio(*_):
            self.escritorio()
            self.fc.vai()
        Texto(self.fc, "Você pega o pendrive e guarde no bolso", foi=self.mostra).vai()
        
        
        

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
        self.codigo = [
        Pista(100, 70, "A única parte que sei é algo como 4-4, deixe eu pensar mais"),
        Pista(600, 150, "Ah, a fórmula do Dr. Frederick tem 5-1, uma das meninas sabe o resto"),
        Pista(750, 140, "Bem, o que você procura tem a ver com 3-2, a Débora deve saber mais"),
        Pista(270, 120, "A Shirley é uma fofoqueira, mas eu posso te contar sobre o 5-1, alguem sabe o resto"),
        Pista(400, 450, "A Joana uma vez falou algo como 2-2, lembro que alguém anotou o resto em algum lugar"),
        Pista(700, 110, "No bloco você lê: Na verdade, tudo está em uma tabela colada no quadro"),
        Pista(700, 110, "Você pega a tabela colada no quadro, talvez você possa decifrar algo"),
        ]
        self.fc = Cena(FREDERICK, direita=self, meio=self, esquerda=self)
        self.tabela = Elemento(TABELA, x=720, y=130, w=60, h=60, cena=self.fc)
        self.ajuda.elt.style.opacity = 0.01
        self.inicia = self.vai
        self.inicia_pista()
        
    def inicia_pista(self, *_):
        p = self.codigo[0]
        self.dica = 0
        self.ajuda = Elemento(FOCO, x=p.x, y=p.y, w=150, h=150, cena=self.fc,vai=self.pista)
        self.tabela.elt.style.left = 720
        self.tabela.elt.style.top = 130
        self.tabela.elt.style.width = 60
        self.tabela.elt.style.height = "60px"
        
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
            self.tabela.elt.style.height = "500px"
            self.tabela.vai = self.inicia_pista
        
    def vai(self, *_):
        self.fc.vai()
        Texto(self.fc, "Você chegou ao lab do Dr.Frederick, procure pistas da fórmula").vai()

def grace():
    fc = FioCruz()
    fc = LembrarHerdeitariedade()
    #fc = EntenderHerdeitariedade()
    fc.inicia()
    
    
if __name__ == "__main__":
    grace()