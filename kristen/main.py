# irene.kristen.main.py
"""Planejamento do jogo da Genética JAIE19
"""
__author__ = "<Cristiane Jorge cristiane.bonfim@ifb.edu.br>"
__version__ = "19.11.11"
from _spy.vitollino.main import STYLE, Cena, Elemento, Texto
STYLE.update(width=850, height="650px") # Atualiza o tamanho da tela
FOCO = "https://i.imgur.com/6e096Va.png"
FIOCRUZ = "https://i.imgur.com/pJDyRCt.jpg"

class FioCruz:
	""" Cenário da FioCruz. """
	def __init__(self):
		self.fiocruz = Cena(FIOCRUZ)
		self.ajuda = Elemento(FOCO, x=75, y=405, cena=self.fiocruz, style={"opacity": 0, "width": "50px", "height": "50px"}, vai=self._ajuda)

	def _ajuda(self, _=0):
		"""O personagem dá uma explicação  de como encontrar o lab"""
		Texto(self.fiocruz, "O laboratóiro? Siga pela esquerda").vai()

	def inicia(self):
		"""O jogo inicia aqui. O cenário principal será apresentado """
		self.fiocruz.vai()
		Texto(self.fiocruz, "Temos que achar o laboratorio. Vamos perguntas a alguém").vai()


if __name__ == "__main__":
	fc = FioCruz()
	fc.inicia()