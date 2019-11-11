
{'date': 'Mon Nov 11 2019 10:37:34.473 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 17
  self.ajuda = Elemento(FOCO, x=100, y=500 cena=self.fiocruz)
                                            ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Nov 11 2019 10:43:52.961 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 15
  def __init__(self):
  ^
IndentationError: unexpected indent
'''},
{'date': 'Mon Nov 11 2019 10:48:35.575 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 19
  def ajuda_personagem(self, _=0)
                                  ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Nov 11 2019 10:51:54.997 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 17
  self.dica_inicial = Elemento(FOCO, x=30, y=360, cena=self.fiocruz, 
                                                                                                   ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Nov 11 2019 10:52:33.693 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 32
    fc = FioCruz()
  module <module> line 17
    self.dica_inicial = Elemento(FOCO, x=30, y=360, cena=self.fiocruz, 
  module _spy.vitollino.main line 536
    self.style.update(**style)
AttributeError: 'set' object has no attribute '__getitem__'
'''},