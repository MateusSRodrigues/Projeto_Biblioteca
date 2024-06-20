'''from .pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome=None, email=None, cpf=None, endereco=None, senha=None, n_inscricao=None):
        super().__init__(nome, email, cpf, endereco, senha)
        if n_inscricao == None:
            while True:
                try:
                    n_inscricao = input("Digite o número de inscrição: ")
                    if n_inscricao.strip():
                        self._n_inscricao = n_inscricao
                        break
                    else:
                        raise ValueError("O numero não pode ser vazio.")
                except ValueError as e:
                    print(e)

#teste = Professor()
'''


from .pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome=None, email=None, cpf=None, endereco=None, senha=None, n_inscricao=None):
        """
        Construtor da classe Professor.

        Args:
            nome (str): Nome do professor.
            email (str): Endereço de email do professor.
            cpf (str): CPF do professor.
            endereco (str): Endereço do professor.
            senha (str): Senha do professor.
            n_inscricao (str): Número de inscrição do professor.
        """
        super().__init__(nome, email, cpf, endereco, senha)
        if n_inscricao is None:
            self._init_interactive_n_inscricao()
        else:
            self._n_inscricao = n_inscricao

    def _init_interactive_n_inscricao(self):
        """
        Método interativo para inicializar o número de inscrição do professor.
        """
        while True:
            try:
                n_inscricao = input("Digite o número de inscrição: ")
                if n_inscricao.strip():  # Verifica se a string não está vazia após remover espaços em branco
                    self._n_inscricao = n_inscricao
                    break  # Sai do loop se o nome for válido
                else:
                    raise ValueError("O número de inscrição não pode ser vazio.")
            except ValueError as e:
                print(e)

    @property
    def n_inscricao(self):
        """
        Propriedade que retorna o número de inscrição do professor.
        """
        return self._n_inscricao

    @n_inscricao.setter
    def n_inscricao(self, novo_n_inscricao):
        """
        Setter da propriedade n_inscricao. Valida e define o novo valor do número de inscrição.

        Args:
            novo_n_inscricao (str): Novo valor do número de inscrição.
        """
        if not novo_n_inscricao.strip():
            raise ValueError("O número de inscrição não pode ser vazio.")

        self._n_inscricao = novo_n_inscricao

    def __str__(self):
        """
        Método de representação em string da classe Professor.
        """
        return f"\nProfessor: \n{super().__str__()}\nNúmero de Inscrição: {self._n_inscricao}"
