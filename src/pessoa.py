class Pessoa:
    def __init__(self, nome=None, email=None, cpf=None, endereco=None, senha=None):
        if nome is None or email is None or cpf is None or endereco is None or senha is None:
            self._sup_interactive()
        else:
            self.nome = nome
            self.email = email
            self.cpf = cpf
            self.endereco = endereco
            self.senha = senha

    def _sup_interactive(self):
        # Nome
        while True:
            try:
                nome = input("Digite o nome: ")
                if nome.strip():
                    self.nome = nome
                    break
                else:
                    raise ValueError("O nome não pode ser vazio.")
            except ValueError as e:
                print(e)

        # Email
        while True:
            try:
                email = input("Digite o email: ")
                if email.strip():
                    self.email = email
                    break
                else:
                    raise ValueError("O email não pode ser vazio.")
            except ValueError as e:
                print(e)

        # CPF
        while True:
            try:
                cpf = input("Digite o CPF: ")
                if cpf.strip():
                    self.cpf = cpf
                    break
                else:
                    raise ValueError("O CPF não pode ser vazio.")
            except ValueError as e:
                print(e)

        # Endereço
        while True:
            try:
                endereco = input("Digite o endereço: ")
                if endereco.strip():
                    self.endereco = endereco
                    break
                else:
                    raise ValueError("O endereço não pode ser vazio.")
            except ValueError as e:
                print(e)

        # Senha
        while True:
            try:
                senha = input("Digite a senha: ")
                if senha.strip():
                    self.senha = senha
                    break
                else:
                    raise ValueError("A senha não pode ser vazia.")
            except ValueError as e:
                print(e)
