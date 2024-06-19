from datetime import date
from .obrafisica import ObraFisica

class TrabalhoAcademico(ObraFisica):
    def __init__(self, titulo=None, autor=None, data_publicacao=None, paginas=None, quantidade=None, exemplar=None, estado=None, tipo=None, orientador=None, nivel_academico=None, area_estudo=None):
        if titulo is None or autor is None or data_publicacao is None or paginas is None or quantidade is None or exemplar is None or estado is None or tipo is None or orientador is None or nivel_academico is None or area_estudo is None:
            self._init_interactive()
        else:
            super().__init__(titulo, autor, data_publicacao, paginas, quantidade, exemplar, estado)
            self.tipo = tipo
            self.orientador = orientador
            self.nivel_academico = nivel_academico
            self.area_estudo = area_estudo

    def _init_interactive(self):
        # Inicialização interativa para os atributos da classe base
        super()._init_interactive()

        # Tipo
        while True:
            try:
                tipo = input("Digite o tipo do trabalho acadêmico: ")
                if tipo.strip():
                    self.tipo = tipo
                    break
                else:
                    raise ValueError("O tipo não pode ser vazio.")
            except ValueError as e:
                print(e)
        
        # Orientador
        while True:
            try:
                orientador = input("Digite o nome do orientador: ")
                if orientador.strip():
                    self.orientador = orientador
                    break
                else:
                    raise ValueError("O orientador não pode ser vazio.")
            except ValueError as e:
                print(e)
        
        # Nível Acadêmico
        while True:
            try:
                nivel_academico = input("Digite o nível acadêmico: ")
                if nivel_academico.strip():
                    self.nivel_academico = nivel_academico
                    break
                else:
                    raise ValueError("O nível acadêmico não pode ser vazio.")
            except ValueError as e:
                print(e)
        
        # Área de Estudo
        while True:
            try:
                area_estudo = input("Digite a área de estudo: ")
                if area_estudo.strip():
                    self.area_estudo = area_estudo
                    break
                else:
                    raise ValueError("A área de estudo não pode ser vazia.")
            except ValueError as e:
                print(e)

    @classmethod
    def from_db(cls, titulo, autor, data_publicacao, paginas, quantidade, exemplar, estado, tipo, orientador, nivel_academico, area_estudo):
        instance = cls(titulo, autor, data_publicacao, paginas, quantidade, exemplar, estado, tipo, orientador, nivel_academico, area_estudo)
        return instance

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, novo_tipo):
        if isinstance(novo_tipo, str) and novo_tipo.strip():
            self._tipo = novo_tipo
        else:
            raise ValueError("O tipo deve ser uma string não vazia.")

    @property
    def orientador(self):
        return self._orientador

    @orientador.setter
    def orientador(self, novo_orientador):
        if isinstance(novo_orientador, str) and novo_orientador.strip():
            self._orientador = novo_orientador
        else:
            raise ValueError("O orientador deve ser uma string não vazia.")

    @property
    def nivel_academico(self):
        return self._nivel_academico

    @nivel_academico.setter
    def nivel_academico(self, novo_nivel_academico):
        if isinstance(novo_nivel_academico, str) and novo_nivel_academico.strip():
            self._nivel_academico = novo_nivel_academico
        else:
            raise ValueError("O nível acadêmico deve ser uma string não vazia.")

    @property
    def area_estudo(self):
        return self._area_estudo

    @area_estudo.setter
    def area_estudo(self, nova_area_estudo):
        if isinstance(nova_area_estudo, str) and nova_area_estudo.strip():
            self._area_estudo = nova_area_estudo
        else:
            raise ValueError("A área de estudo deve ser uma string não vazia.")

    def retornar_atributos(self):
        return super().retornar_sup() + [self._tipo, self._orientador, self._nivel_academico, self._area_estudo]
