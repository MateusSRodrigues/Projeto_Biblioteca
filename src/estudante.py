'''from pessoa import Pessoa
from comum import Comum

class EstudanteGraduacao(Pessoa, Comum):
    def __init__(self, nome, email, cpf, endereco, saldo, senha, matricula, curso):
        super().__init__(nome, email, cpf, endereco, saldo, senha)
        self._matricula = matricula
        self._curso = curso
'''

from pessoa import Pessoa
from comum import Comum

class Estudante(Pessoa, Comum):
    def __init__(self, nome, email, cpf, endereco, saldo, senha, matricula, curso):
        """
        Construtor da classe Estudante.

        Args:
            nome (str): Nome do estudante.
            email (str): Endereço de email do estudante.
            cpf (str): CPF do estudante.
            endereco (str): Endereço do estudante.
            saldo (float): Saldo do estudante.
            senha (str): Senha do estudante.
            matricula (str): Número de matrícula do estudante.
            curso (str): Curso do estudante.
        """
        super().__init__(nome, email, cpf, endereco, saldo, senha)
        self._matricula = matricula
        self._curso = curso

    def consultar_matricula(self) -> str:
        """
        Consulta o número de matrícula do estudante.

        Returns:
            str: Número de matrícula do estudante.
        """
        return self._matricula

    def consultar_curso(self) -> str:
        """
        Consulta o curso do estudante.

        Returns:
            str: Curso do estudante.
        """
        return self._curso

    def pedir_reserva(self, obra: Livro) -> bool:
        """
        Tenta reservar um livro para o estudante.

        Args:
            obra (Livro): Objeto Livro que representa o livro a ser reservado.

        Returns:
            bool: True se a reserva for bem-sucedida, False caso contrário.
        """
        if self.saldo >= obra.preco_locacao:
            self.saldo -= obra.preco_locacao
            return True
        else:
            return False

    def registrar_emprestimo(self, obra: ObraFisica) -> bool:
        """
        Registra o empréstimo de uma obra física para o estudante.

        Args:
            obra (ObraFisica): Objeto ObraFisica que representa a obra física a ser emprestada.

        Returns:
            bool: True se o empréstimo for bem-sucedido, False caso contrário.
        """
        if self.saldo >= obra.preco_locacao:
            self.saldo -= obra.preco_locacao
            return True
        else:
            return False

    def registrar_devolucao(self, obra: ObraFisica) -> bool:
        """
        Registra a devolução de uma obra física pelo estudante.

        Args:
            obra (ObraFisica): Objeto ObraFisica que representa a obra física a ser devolvida.

        Returns:
            bool: True se a devolução for bem-sucedida, False caso contrário.
        """
        self.saldo += obra.preco_locacao
        return True

    def renovar_emprestimo(self, obra: ObraFisica) -> bool:
        """
        Tenta renovar o empréstimo de uma obra física para o estudante.

        Args:
            obra (ObraFisica): Objeto ObraFisica que representa a obra física a ser renovada.

        Returns:
            bool: True se a renovação for bem-sucedida, False caso contrário.
        """
        if self.saldo >= obra.preco_renovacao:
            self.saldo -= obra.preco_renovacao
            return True
        else:
            return False
