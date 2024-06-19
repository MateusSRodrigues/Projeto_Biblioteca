from .pessoa import Pessoa

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