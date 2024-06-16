from datetime import date
from datetime import datetime

class ObraFisica:
    def __init__(self, titulo=None, autor=None, data_publicacao=None, paginas=None, quantidade=None):
        if titulo is None or autor is None or data_publicacao is None or paginas is None or quantidade is None:
            self._sup_interactive()
        else:
            self.titulo = titulo
            self.autor = autor
            self.data_publicacao = data_publicacao
            self.paginas = paginas
            self.quantidade = quantidade
            #self.exemplar = exemplar
            #self.estado = estado

    def _sup_interactive(self):
        # Título
        while True:
            try:
                titulo = input("Digite o título da obra: ")
                if titulo.strip():
                    self.titulo = titulo
                    break
                else:
                    raise ValueError("O título não pode ser vazio.")
            except ValueError as e:
                print(e)
        
        # Autor
        while True:
            try:
                autor = input("Digite o autor da obra: ")
                if autor.strip():
                    self.autor = autor
                    break
                else:
                    raise ValueError("O autor não pode ser vazio.")
            except ValueError as e:
                print(e)
        
        # Data de Publicação
        while True:
            try:
                data_publicacao = input("Digite a data de publicação (AAAA-MM-DD): ")
                self.data_publicacao = date.fromisoformat(data_publicacao)
                break
            except ValueError as e:
                print("Data inválida. Use o formato AAAA-MM-DD.")
        
        # Páginas
        while True:
            try:
                paginas = input("Digite o número de páginas: ")
                if paginas.isdigit():
                    self.paginas = int(paginas)
                    break
                else:
                    raise ValueError("O número de páginas deve ser um número inteiro.")
            except ValueError as e:
                print(e)
        
        # Quantidade
        while True:
            try:
                quantidade = input("Digite a quantidade: ")
                if quantidade.isdigit():
                    self.quantidade = int(quantidade)
                    break
                else:
                    raise ValueError("A quantidade deve ser um número inteiro.")
            except ValueError as e:
                print(e)
        
        # Exemplar
        while True:
            try:
                exemplar = input("Digite o exemplar: ")
                if exemplar.strip():
                    self.exemplar = exemplar
                    break
                else:
                    raise ValueError("O exemplar não pode ser vazio.")
            except ValueError as e:
                print(e)
        
        # Estado
        while True:
            try:
                estado = input("Digite o estado da obra: ")
                if estado.strip():
                    self.estado = estado
                    break
                else:
                    raise ValueError("O estado não pode ser vazio.")
            except ValueError as e:
                print(e)

    @classmethod
    def from_db(cls, titulo, autor, data_publicacao, paginas, quantidade, exemplar, estado):
        instance = cls(titulo, autor, data_publicacao, paginas, quantidade, exemplar, estado)
        return instance

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        if isinstance(novo_titulo, str) and novo_titulo.strip():
            self._titulo = novo_titulo
        else:
            raise ValueError("O título deve ser uma string não vazia.")
    
    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, novo_autor):
        if isinstance(novo_autor, str) and novo_autor.strip():
            self._autor = novo_autor
        else:
            raise ValueError("O autor deve ser uma string não vazia.")
    
    @property
    def data_publicacao(self):
        return self._data_publicacao

    @data_publicacao.setter
    def data_publicacao(self, nova_data):
        try:
            # Tenta converter a string em um objeto datetime.date
            self._data_publicacao = datetime.strptime(nova_data, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Formato de data inválido. Use AAAA-MM-DD.")
    
    @property
    def paginas(self):
        return self._paginas

    @paginas.setter
    def paginas(self, novas_paginas):
        if isinstance(novas_paginas, int) and novas_paginas > 0:
            self._paginas = novas_paginas
        else:
            raise ValueError("O número de páginas deve ser um inteiro positivo.")
    
    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, nova_quantidade):
        if isinstance(nova_quantidade, int) and nova_quantidade >= 0:
            self._quantidade = nova_quantidade
        else:
            raise ValueError("A quantidade deve ser um inteiro não negativo.")
    
    @property
    def exemplar(self):
        return self._exemplar

    @exemplar.setter
    def exemplar(self, novo_exemplar):
        if isinstance(novo_exemplar, str) and novo_exemplar.strip():
            self._exemplar = novo_exemplar
        else:
            raise ValueError("O exemplar deve ser uma string não vazia.")
    
    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, novo_estado):
        if isinstance(novo_estado, str) and novo_estado.strip():
            self._estado = novo_estado
        else:
            raise ValueError("O estado deve ser uma string não vazia.")
    
    def retornar_sup(self):
        return [self._titulo, self._autor, self._data_publicacao, self._paginas, self._quantidade]
    
    def retornar_atributos():
        pass