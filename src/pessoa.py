class Pessoa:
    def __init__(self, nome=None, email=None, cpf=None, endereco=None, senha=None):
        if nome is None or email is None or cpf is None or endereco is None or senha is None:
            self._sup_interactive()
        else:
            self._nome = nome
            self._email = email
            self._cpf = cpf
            self._endereco = endereco
            self._senha = senha

    def _sup_interactive(self):
        # Nome-32
        while True:
            try:
                nome = input("Digite o nome: ")
                if nome.strip():
                    self._nome = nome
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
                    self._email = email
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
                    self._cpf = cpf
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

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
        @property
        
    def email(self):
        return self._email
    
    @email.setter
    def email(self, novo_email):
        self._email = novo_email
        
    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, novo_cpf):
        self._cpf = novo_cpf
        
    @property   
    def endereco(self):
        return self._endereco
    
    @endereco.setter
    def endereco(self, novo_endereco):
        self._endereco = novo_emendereco
        
    @property   
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, nova_senha):
        self._senha = nova_senha



