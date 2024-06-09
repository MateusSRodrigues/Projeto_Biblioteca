from obrafisica import ObraFisica
from datetime import date

class Livro(ObraFisica):
    def __init__(self, titulo, autor, data_publicacao, paginas, quantidade, exemplar, estado, ISBN, editora, genero, valor):
        super().__init__(titulo, autor, data_publicacao, paginas, quantidade, exemplar, estado)
        self._ISBN = ISBN
        self._editora = editora
        self._genero = genero
        self._valor = valor

    @property
    def ISBN(self):
        return self._ISBN

    @property
    def editora(self):
        return self._editora

    @property
    def genero(self):
        return self._genero

    @property
    def valor(self):
        return self._valor

    def method(self, type):
        if type == "calcular_multa":
            # Lógica para calcular multa de atraso (exemplo)
            dias_atraso = (date.today() - self._data_publicacao).days
            multa = dias_atraso * 0.50  # R$0.50 por dia de atraso
            return multa
        else:
            return "Método não implementado para este tipo"

    def __str__(self):
        return super().__str__() + f"\nISBN: {self._ISBN}\nEditora: {self._editora}\nGênero: {self._genero}\nValor: R${self._valor:.2f}"
