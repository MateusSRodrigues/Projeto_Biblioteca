from pessoa import Pessoa

class EstudanteGraduacao(Pessoa):
    def __init__(self, nome, email, cpf, endereco, saldo, senha, matricula, curso):
        super().__init__(nome, email, cpf, endereco, saldo, senha)
        self._matricula = matricula
        self._curso = curso
