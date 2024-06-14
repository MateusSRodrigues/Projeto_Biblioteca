from obrafisica import ObraFisica

class Periodico(ObraFisica):
  def __init__(self, titulo, autor, data_publicacao, paginas, quantidade, exemplar, estado, ISSN, editora, area_estudo, volume):
      super().__init__(titulo, autor, data_publicacao, paginas, quantidade, exemplar, estado)
      self._ISSN = ISSN
      self._editora = editora
      self._area_estudo = area_estudo
      self._volume = volume
