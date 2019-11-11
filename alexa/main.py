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
FREDERICK = "https://i.imgur.com/4EtsjiX.jpg"

class FioCruz:
    """ Cenário da FioCruz. """
    def __init__(self):
        self.fiocruz = Cena(FIOCRUZ)
        self.dica_inicial = Elemento(FOCO, x=50, y=380, cena=self.fiocruz, 
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
        self.dica_inicial = Elemento(FOCO, x=50, y=380, cena=self.lab, 
            style={"opacity": 0.1}, vai=self.ajuda_personagem)

    def ajuda_personagem(self, _=0):
        """O personagem dará uma dica de como encontrar o lab."""
        Texto(self.lab, "Para encontrar o lab, você precisa seguir para esquerda...").vai()
        

    def inicia(self):
        """O jogo inicia aqui. O cenário principal será apresentado """
        self.lab.vai()
        Texto(self.lab, "Precisamos encontrar o lab. Quem tem boca vai a Roma!").vai()