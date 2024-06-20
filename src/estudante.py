from pessoa import Pessoa
from comum import Comum

class Estudante(Pessoa, Comum):
    def __init__(self, nome=None, email=None, cpf=None, endereco=None, senha=None, matricula=None):
        super().__init__(nome, email, cpf, endereco, senha)
        if matricula == None:
            while True:
                try:
                    matricula = input("Digite o número de inscrição: ")
                    if matricula.strip():
                        self._matricula = matricula
                        break
                    else:
                        raise ValueError("O numero não pode ser vazio.")
                except ValueError as e:
                    print(e)

#teste = Estudante()