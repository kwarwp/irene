
{'date': 'Wed Nov 06 2019 08:47:06.286 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 59
  self.decide.update(s:self.entra)
                       ^
SyntaxError: invalid syntax
'''},
{'date': 'Wed Nov 06 2019 08:47:27.580 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 67
  input("Uma sábia decisão, seria loucura explorar este templo macabro!)]
                                                                         ^
SyntaxError: EOL while scanning string literal
'''},
{'date': 'Wed Nov 06 2019 08:47:39.673 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 67
  input("Uma sábia decisão, seria loucura explorar este templo macabro!)
                                                                        ^
SyntaxError: EOL while scanning string literal
'''},
{'date': 'Wed Nov 06 2019 09:16:59.260 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 42
  for camara in range(self.quantidade)
                                       ^
SyntaxError: invalid syntax
'''},
{'date': 'Wed Nov 06 2019 09:17:17.875 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 95
    TemploInca().inicia()
  module <module> line 80
    self.decide[input("Uma expedição para coletar os tesouros do Templo Inca. Você vai explorar o templo (s/N)?")]()
  module <module> line 88
    self.camara.explora(self.explorador)
  module <module> line 43
    self.decide[input("Você entra em uma câmara com tesouros! Continua?").lower()]()
  module <module> line 68
    explorador.pega(randint(1, 4), self)
  module <module> line 26
    camara.entra(self)
TypeError: entra() takes 1 positional argument but more were given
'''},
{'date': 'Thu Nov 07 2019 12:19:32.398 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 147
  def apresenta(self, texto, valores, acoes=None)
                                                  ^
SyntaxError: invalid syntax
'''},
{'date': 'Thu Nov 07 2019 12:19:58.344 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 151
  def falha(self, *_, **_):
                        ^
SyntaxError: duplicate argument _ in function definition
'''},
{'date': 'Thu Nov 07 2019 12:24:22.715 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 190
    TemploInca().inicia()
  module <module> line 175
    self.apresenta("Uma expedição para saquear o Templo Inca. Vai encarar (s/N)?")
TypeError: apresenta missing 1 positional argument: 'valores'
'''},
{'date': 'Thu Nov 07 2019 12:26:41.727 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 191
    TemploInca().inicia()
  module <module> line 176
    self.apresenta("Uma expedição para saquear o Templo Inca. Vai encarar (s/N)?")
  module <module> line 150
    self.decide(self.renderizador(texto.format(valores)))
TypeError: 'defaultdict' object is not callable
'''},
{'date': 'Thu Nov 07 2019 12:27:06.11 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 150
  self.decide(self.renderizador(texto)
                                                     ^
SyntaxError: invalid syntax
'''},
{'date': 'Thu Nov 07 2019 13:59:57.853 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 194
    TemploInca().inicia()
  module <module> line 179
    self.apresenta("Uma expedição para saquear o Templo Inca. Vai encarar (s/N)?")
  module <module> line 36
    self.decide[self.renderizador(texto)](*args, **kwargs)
  module <module> line 183
    self.camara.entra(self.explorador)
  module <module> line 107
    self.decide[o_que_decidiu.lower()](explorador)
  module <module> line 112
    self.decide[self.quantidade](explorador)
  module <module> line 117
    explorador.pega(randint(1, 4), self.baralho.proximo())
  module <module> line 73
    self.ui.apresenta(texto, dict(quantidade= quantidade, mochila=self.mochila))
  module <module> line 33
    texto = texto.format(valores) if valores else texto
KeyError: quantidade
'''},
{'date': 'Thu Nov 07 2019 14:33:57.326 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 195
    TemploInca().inicia()
  module <module> line 180
    self.apresenta("Uma expedição para saquear o Templo Inca. Vai encarar (s/N)?")
  module <module> line 36
    self.decide[self.renderizador(texto)](*args, **kwargs)
  module <module> line 184
    self.camara.entra(self.explorador)
  module <module> line 108
    self.decide[o_que_decidiu.lower()](explorador)
  module <module> line 113
    self.decide[self.quantidade](explorador)
  module <module> line 118
    explorador.pega(randint(1, 4), self.baralho.proximo())
  module <module> line 73
    texto = "Você coloca {quantidade} pedras na mochila e fica com {mochila} tesouros".format(form)
KeyError: quantidade
'''},
{'date': 'Thu Nov 07 2019 14:34:18.994 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <SyntaxError: missing ) after argument list>
'''},
{'date': 'Thu Nov 07 2019 14:34:24.339 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <SyntaxError: missing ) after argument list>
'''},