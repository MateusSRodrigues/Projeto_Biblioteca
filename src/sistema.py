import os,termios, sys, tty

class Sistema:
    def login(self):
        cpf = input("CPF: ")
        senha = input("Senha: ")
        #chama a funçao que consultarcadastro(cpf,senha)
        # if "funcao consultar cadastro" retornar false chama menu inicial de novo
        # else cria uma pessoa(adm,graduando...) e chama a sua funcao menu 

    def cadastrar(self):
        nome = input("Nome: ")
        email = input("Email: ")
        cpf = input("CPF: ")
        endereco = input("Endereco: ")
        saldo = input("Saldo")
        senha = input("Senha: ")
        #chama a funçao consultar
        #se ja existir manda msg de erro e chama o menu denovo
        #se nao chama a funcao cadastrar do banco de dados

    
    def menuInicial(self):
        def get_char():        # Função para capturar o caractere pressionado pelo usuário
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch
        c = 0
        while True:
            opcao = ["Login", "Cadastrar", "Pesqisar obra"]
            cabecalho = ["Pressione 'W' para subir 'S' para descer e 'D' para selecionar.\n", "O que deseja Fazer?"]
            os.system('clear')
            os.system('cls' if os.name == 'nt' else 'clear')        

            for i in range(len(opcao)):
                if i == 0:
                    for item in cabecalho:
                        print(item, end='')
                    print("\n------------------------------")
                if i == c % len(opcao):
                    print(f"->{opcao[i]}")
                else:
                    print(opcao[i])
                if i == len(opcao) - 1:
                    print("====================================\n====================================")

            n = get_char()

            if n == 's':
                c += 1  # altera contador de click, desce a seta
            elif n == 'w':
                c -= 1  # altera contador de click, sobe a seta
            elif n == 'd':  # escolhe opção
                if c == 0:
                    if opcao[c] == opcao[0]: #Login
                        self.login()

                else:                     #alterar o que cada opçao faz
                    if opcao [c % len(opcao)] == opcao[0]: #Login   
                        self.login()

                    
                    if opcao [c % len(opcao)] == opcao[1]: #Cadastrar
                        self.cadastrar()
                    
                    if opcao [c % len(opcao)] == opcao[2]: #Pesquisar obra
                       #chama a funcao pesquisar obra do banco de dados
