from obrafisica import ObraFisica

class TrabalhoAcademico(ObraFisica):
  def __init__(self, titulo, autor, data_publicacao, paginas, quantidade, exemplar, estado, tipo, orientador,nivel_academico, area_estudo):
      super().__init__(titulo, autor, data_publicacao, paginas, quantidade, exemplar, estado)
      self._tipo = tipo
      self._orientador = orientador
      self._nivel_academico = nivel_academico
      self._area_estudo = area_estudo
