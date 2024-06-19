from datetime import date
from .obrafisica import ObraFisica

class Periodico(ObraFisica):
    def __init__(self, titulo=None, autor=None, data_publicacao=None, paginas=None, quantidade=None, exemplar=None, estado=None, ISSN=None, editora=None, area_estudo=None, volume=None):
        if titulo is None or autor is None or data_publicacao is None or paginas is None or quantidade is None or exemplar is None or estado is None or ISSN is None or editora is None or area_estudo is None or volume is None:
            self._init_interactive()
        else:
            super().__init__(titulo, autor, data_publicacao, paginas, quantidade, exemplar, estado)
            self.ISSN = ISSN
            self.editora = editora
            self.area_estudo = area_estudo
            self.volume = volume

    def _init_interactive(self):
        # Inicialização interativa para os atributos da classe base
        super()._sup_interactive()

        # ISSN
        while True:
            try:
                ISSN = input("Digite o ISSN do periódico: ")
                if ISSN.strip():
                    self.ISSN = ISSN
                    break
                else:
                    raise ValueError("O ISSN não pode ser vazio.")
            except ValueError as e:
                print(e)
        
        # Editora
        while True:
            try:
                editora = input("Digite a editora do periódico: ")
                if editora.strip():
                    self.editora = editora
                    break
                else:
                    raise ValueError("A editora não pode ser vazia.")
            except ValueError as e:
                print(e)
        
        # Área de Estudo
        while True:
            try:
                area_estudo = input("Digite a área de estudo do periódico: ")
                if area_estudo.strip():
                    self.area_estudo = area_estudo
                    break
                else:
                    raise ValueError("A área de estudo não pode ser vazia.")
            except ValueError as e:
                print(e)
        
        # Volume
        while True:
            try:
                volume = input("Digite o volume do periódico: ")
                if volume.isdigit():
                    self.volume = int(volume)
                    break
                else:
                    raise ValueError("O volume deve ser um número inteiro.")
            except ValueError as e:
                print(e)

    @classmethod
    def from_db(cls, titulo, autor, data_publicacao, paginas, quantidade, exemplar, estado, ISSN, editora, area_estudo, volume):
        instance = cls(titulo, autor, data_publicacao, paginas, quantidade, exemplar, estado, ISSN, editora, area_estudo, volume)
        return instance

    @property
    def ISSN(self):
        return self._ISSN

    @ISSN.setter
    def ISSN(self, novo_ISSN):
        if isinstance(novo_ISSN, str) and novo_ISSN.strip():
            self._ISSN = novo_ISSN
        else:
            raise ValueError("O ISSN deve ser uma string não vazia.")

    @property
    def editora(self):
        return self._editora

    @editora.setter
    def editora(self, nova_editora):
        if isinstance(nova_editora, str) and nova_editora.strip():
            self._editora = nova_editora
        else:
            raise ValueError("A editora deve ser uma string não vazia.")

    @property
    def area_estudo(self):
        return self._area_estudo

    @area_estudo.setter
    def area_estudo(self, nova_area_estudo):
        if isinstance(nova_area_estudo, str) and nova_area_estudo.strip():
            self._area_estudo = nova_area_estudo
        else:
            raise ValueError("A área de estudo deve ser uma string não vazia.")

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, novo_volume):
        if isinstance(novo_volume, int) and novo_volume > 0:
            self._volume = novo_volume
        else:
            raise ValueError("O volume deve ser um inteiro positivo.")

    def retornar_atributos(self):
        return super().retornar_sup() + [self._ISSN, self._editora, self._area_estudo, self._volume]
