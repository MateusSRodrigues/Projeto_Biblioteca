'''from .obrafisica import ObraFisica
from datetime import date

class Livro(ObraFisica):

    def __init__(self, editora=None, ISBN=None, genero=None, titulo=None, autor=None, data_publicacao=None, paginas=None, quantidade=None):
        if editora is None or ISBN is None or genero is None:
            self._init_interactive()
        else:
            self.editora = editora
            self.genero = genero
        
        super().__init__(ISBN, titulo, autor, data_publicacao, paginas, quantidade)

    def _init_interactive(self):
        # Editora
        while True:
            try:
                editora = input("Digite o nome da editora: ")
                if editora.strip():  # Verifica se a string não está vazia após remover espaços em branco
                    self.editora = editora
                    break  # Sai do loop se o nome for válido
                else:
                    raise ValueError("O nome da editora não pode ser vazio.")
            except ValueError as e:
                print(e)
        """
        # ISBN
        while True:
            try:
                ISBN = input("Digite o ISBN do Livro: ")
                if ISBN.strip():  # Verifica se a string não está vazia após remover espaços em branco
                    self.ISBN = ISBN
                    break  # Sai do loop se o nome for válido
                else:
                    raise ValueError("O ISBN não pode ser vazio.")
            except ValueError as e:
                print(e)
        """
        # Genero
        while True:
            try:
                genero = input("Digite o genero do Livro: ")
                if genero.strip():  # Verifica se a string não está vazia após remover espaços em branco
                    self.genero = genero
                    break  # Sai do loop se o nome for válido
                else:
                    raise ValueError("O genero não pode ser vazio.")
            except ValueError as e:
                print(e)
        """
        # Valor
        while True:
            try:
                valor = input("Digite o valor do Livro: ")
                if valor.strip():  # Verifica se a string não está vazia após remover espaços em branco
                    self.valor = valor
                    break  # Sai do loop se o nome for válido
                else:
                    raise ValueError("O valor não pode ser vazio.")
            except ValueError as e:
                print(e)
        
    @property
    def ISBN(self):
        return self._ISBN
    
    @ISBN.setter
    def ISBN(self, novo_ISBN):
        novo_ISBN = novo_ISBN.replace("-", "")  # Remove hífens, se houver

        if not novo_ISBN.isdigit():
            raise ValueError("ISBN deve ser composto apenas por números.")

        if len(novo_ISBN) != 10 and len(novo_ISBN) != 13:
            raise ValueError("ISBN deve ter 10 ou 13 dígitos.")

        self._ISBN = novo_ISBN
    """

    @property
    def editora(self):
        return self._editora
   
    @editora.setter
    def editora(self, novo_nome):
        if isinstance(novo_nome, str) and novo_nome.strip() != "":
            self._editora = novo_nome
        else:
            raise ValueError("Nome deve ser uma string não vazia")
        

    @property
    def genero(self):
        return self._genero
    
    @genero.setter
    def genero(self, novo_genero):

        if novo_genero.isdigit():
            raise ValueError("O genero deve ser composto apenas por letras.")
        
        self._genero = novo_genero

    """
    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self, novo_valor):

        if not novo_valor.isdigit():
            raise ValueError("O valor deve ser composto apenas por numeros.")

        self._valor = novo_valor
    """

    def __str__(self):
        return super().__str__() + f"\nISBN: {super()._id}\nEditora: {self._editora}\nGênero: {self._genero}\n"
    
    def retornar_atributos(self):
        return super().retornar_sup() + [self._editora, self._genero]

#livroteste = Livro()
'''



from .obrafisica import ObraFisica
from datetime import date

class Livro(ObraFisica):

    def __init__(self, editora=None, ISBN=None, genero=None, titulo=None, autor=None, data_publicacao=None, paginas=None, quantidade=None):
        """
        Construtor da classe Livro.

        Args:
            editora (str, opcional): Nome da editora do livro.
            ISBN (str, opcional): ISBN do livro.
            genero (str, opcional): Gênero do livro.
            titulo (str): Título do livro.
            autor (str): Autor do livro.
            data_publicacao (date, opcional): Data de publicação do livro.
            paginas (int, opcional): Número de páginas do livro.
            quantidade (int, opcional): Quantidade de exemplares do livro disponíveis.
        """
        if editora is None or ISBN is None or genero is None:
            self._init_interactive()
        else:
            self.editora = editora
            self.genero = genero
        
        super().__init__(ISBN, titulo, autor, data_publicacao, paginas, quantidade)

    def _init_interactive(self):
        """
        Método interativo para inicializar os atributos do livro.
        """
        # Editora
        while True:
            try:
                editora = input("Digite o nome da editora: ")
                if editora.strip():  # Verifica se a string não está vazia após remover espaços em branco
                    self.editora = editora
                    break  # Sai do loop se o nome for válido
                else:
                    raise ValueError("O nome da editora não pode ser vazio.")
            except ValueError as e:
                print(e)

        # ISBN
        while True:
            try:
                ISBN = input("Digite o ISBN do Livro: ")
                if ISBN.strip():  # Verifica se a string não está vazia após remover espaços em branco
                    self.ISBN = ISBN
                    break  # Sai do loop se o nome for válido
                else:
                    raise ValueError("O ISBN não pode ser vazio.")
            except ValueError as e:
                print(e)

        # Genero
        while True:
            try:
                genero = input("Digite o genero do Livro: ")
                if genero.strip():  # Verifica se a string não está vazia após remover espaços em branco
                    self.genero = genero
                    break  # Sai do loop se o nome for válido
                else:
                    raise ValueError("O genero não pode ser vazio.")
            except ValueError as e:
                print(e)

    @property
    def ISBN(self):
        """
        Propriedade que retorna o ISBN do livro.
        """
        return self._ISBN

    @ISBN.setter
    def ISBN(self, novo_ISBN):
        """
        Setter da propriedade ISBN. Valida e define o novo valor do ISBN.

        Args:
            novo_ISBN (str): Novo valor do ISBN.
        """
        novo_ISBN = novo_ISBN.replace("-", "")  # Remove hífens, se houver

        if not novo_ISBN.isdigit():
            raise ValueError("ISBN deve ser composto apenas por números.")

        if len(novo_ISBN) != 10 and len(novo_ISBN) != 13:
            raise ValueError("ISBN deve ter 10 ou 13 dígitos.")

        self._ISBN = novo_ISBN

    @property
    def editora(self):
        """
        Propriedade que retorna o nome da editora do livro.
        """
        return self._editora

    @editora.setter
    def editora(self, novo_nome):
        """
        Setter da propriedade editora. Valida e define o novo valor da editora.

        Args:
            novo_nome (str): Novo valor do nome da editora.
        """
        if isinstance(novo_nome, str) and novo_nome.strip() != "":
            self._editora = novo_nome
        else:
            raise ValueError("Nome deve ser uma string não vazia")

    @property
    def genero(self):
        """
        Propriedade que retorna o gênero do livro.
        """
        return self._genero

    @genero.setter
    def genero(self, novo_genero):

        if novo_genero.isdigit():
            raise ValueError("O genero deve ser composto apenas por letras.")
        
        self._genero = novo_genero