
{'date': 'Mon Nov 11 2019 09:34:08.946 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 18
  Texto(self.fiocruz, "Procure setor de informações, precisamos encontrar o laboratório!".vai()
                                                                                                                           ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Nov 11 2019 09:35:11.564 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 18
  Texto(self.fiocruz, "Procure setor de informações, precisamos encontrar o laboratório!".vai()
                                                                                                                           ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Nov 11 2019 09:42:28.272 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 16
  Texto(self.fiocruz, "O laboratório? Siga pela esquerda").vai()
  ^
IndentationError: unexpected indent
'''},
{'date': 'Mon Nov 11 2019 09:43:26.743 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 16
  Texto(self.fiocruz, "O laboratório? Siga pela esquerda"),vai()
  ^
IndentationError: unexpected indent
'''},
{'date': 'Mon Nov 11 2019 09:48:45.300 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 24
    fc = FioCruz()
  module <module> line 14
    self.ajuda = Elemento(FOCO, x=30, y=350, cena=self.fiocruz, vai=self._äjuda)
AttributeError: 'FioCruz' object has no attribute '_äjuda'
'''},