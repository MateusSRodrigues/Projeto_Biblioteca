from pessoa import Pessoa
from comum import Comum

class EstudanteGraduacao(Pessoa, Comum):
    def __init__(self, nome, email, cpf, endereco, saldo, senha, matricula, curso):
        super().__init__(nome, email, cpf, endereco, saldo, senha)
        self._matricula = matricula
        self._curso = curso
