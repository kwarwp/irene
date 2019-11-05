
{'date': 'Tue Nov 05 2019 12:38:21.617 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 5
  __version__ "19.11.05"
               ^
SyntaxError: invalid syntax
'''},
{'date': 'Tue Nov 05 2019 12:38:38.252 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 7
    STYLE.update(width="1850px", height="650px")
AttributeError: 'module' object has no attribute 'update'
'''},