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
        self._comentarios = []

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
        if isinstance(novo_autor, list) and all(isinstance(a, str) and a.strip() for a in novo_autor):
            self._autor = novo_autor
        else:
            raise ValueError("O autor deve ser uma string não vazia.")
    
    @property
    def data_publicacao(self):
        return self._data_publicacao
    
    @data_publicacao.setter
    def data_publicacao(self, nova_data):
        if isinstance(nova_data, str):
            # Tenta converter a string em um objeto datetime.date
            try:
                self._data_publicacao = datetime.strptime(nova_data, "%Y-%m-%d").date()
            except ValueError:
                raise ValueError("Formato de data inválido. Use AAAA-MM-DD.")
        elif isinstance(nova_data, date):
            # Se já for um objeto datetime.date, apenas atribui
            self._data_publicacao = nova_data
        else:
            raise ValueError("A data deve ser uma string no formato AAAA-MM-DD ou um objeto datetime.date.")
    
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
        if not isinstance(nova_quantidade, int) or nova_quantidade < 0:
            raise ValueError("A quantidade deve ser um inteiro não negativo.")
        self._quantidade = nova_quantidade
    
        # Limpar exemplares existentes (se houver)
        self._exemplar = {}

        # Adicionar exemplares iniciais
        for i in range(1, nova_quantidade + 1):
            self._exemplar[i] = "disponível"

    @property
    def exemplar(self):
        return self._exemplar
    
    @exemplar.setter
    def exemplar(self, id_exemplar):
        if not isinstance(id_exemplar, int):
            raise ValueError("O ID do exemplar deve ser um número inteiro.")
        if id_exemplar in self._exemplar:
            raise ValueError(f"O exemplar com ID {id_exemplar} já existe.")
        self._exemplar[id_exemplar] = "disponível"


    
    @property
    def comentarios(self):
        return self._comentarios

    @comentarios.setter
    def comentarios(self, novo_comentario):
        if isinstance(novo_comentario, str) and novo_comentario.strip():
            self._comentarios.append(novo_comentario) 
        else:
            raise ValueError("O comentario nao pode ser vazio.")
    
    def retornar_sup(self):
        return [self._titulo, self._autor, self._data_publicacao, self._paginas, self._quantidade]
    
    def retornar_atributos():
        pass

    def alterar_estado_exemplar(self, id_exemplar, novo_estado):
        """Altera o estado de um exemplar existente."""
        estados_validos = ["disponível", "emprestado", "reservado"]
        if id_exemplar not in self._exemplar:
            raise ValueError(f"O exemplar com ID {id_exemplar} não existe.")
        if novo_estado not in estados_validos:
            raise ValueError("Estado inválido. Use 'disponível', 'emprestado' ou 'reservado'.")
        self._exemplar[id_exemplar] = novo_estado