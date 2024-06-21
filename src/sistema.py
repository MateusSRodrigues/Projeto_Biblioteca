from .obrafisica import ObraFisica

from .pessoa import Pessoa
import os,termios, sys, tty
import time

class Sistema:
    def login(self) -> None:
        from .gerenciamentodados import GerenciamentoDados
        from .estudante import Estudante
        from .administrador import Administrador
        from .professor import Professor
        from .comum import Comum
        
        while True:
            cpf = input("CPF: ")
            usuario = GerenciamentoDados.procurarCadastro(cpf)
            if usuario:
                senha_digitada = input("Senha: ")
                
                while senha_digitada != usuario.senha:
                    print("Senha incorreta. Tente novamente.")
                    senha_digitada = input("Senha: ")
                
                print("Login bem-sucedido!")
                time.sleep(2)
                if isinstance(usuario, Estudante) or isinstance(usuario, Professor): 
                    Comum.menuUsuario(usuario)
                elif isinstance(usuario, Administrador):
                    usuario.menuUsuario()
            else:
                print("Usuário não encontrado. Verifique o CPF e tente novamente.")
                time.sleep(3)
                self.menuInicial()

                

            #chama a funçao que consultarcadastro(cpf,senha)
            # if "funcao consultar cadastro" retornar false chama menu inicial de novo
            # else cria uma pessoa(adm,graduando...) e chama a sua funcao menu 
    

    def cadastrar(self) -> None:
        from .estudante import Estudante
        from .administrador import Administrador
        from .professor import Professor
        aux = input(print("Você é estudante, professor ou administrador?"))
        if aux == 'estudante':
            pessoa = Estudante() 
        elif aux == 'professor':
            pessoa = Professor
        elif aux == 'administrador': pessoa = Administrador()
        else: print('Tente novamente')

        from .gerenciamentodados import GerenciamentoDados
        GerenciamentoDados.inserirCadastro(pessoa)
    

    def menuInicial(self) -> None:
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
            opcao = ["Login", "Cadastrar", "Pesquisar obra"]
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
                        self.procurarObra()    

                        time.sleep(7)

    def selecionar(self, lista: list[ObraFisica]):
        for index, obra in enumerate(lista, start=1):
            print(f"{index}: {obra.titulo}, {obra.autor}")
        
        indice = int(input(print("Escolha a obra pelo numero indexado:")))
        if 1 <= indice <= len(lista):
            return lista[indice - 1]
        else:
            raise IndexError("Índice fora do intervalo válido")
        
    def procurarObra(self):
        os.system('clear')
        #from gerenciamentodados import GerenciamentoDados

        try:
            titulo = input(print("Digite o titulo da obra:"))
            titulo = str(titulo)
            if not titulo:
                raise ValueError("O titulo não pode ser vazio.")
            else:
                from .gerenciamentodados import GerenciamentoDados
                aux = GerenciamentoDados.pesquisarObraPorTitulo(titulo)
                
                if aux != []:
                    result = self.selecionar(aux)
                    print(result.retornar_atributos())
        except ValueError as e:
            print(e)
            input("Pressione enter para tentar novamente.")
            os.system("clear")



teste = Sistema()
teste.menuInicial()
